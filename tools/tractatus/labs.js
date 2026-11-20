    // =========================================================================
    // INTERACTIVE LABORATORIES, TREE VIEW & QUICK-PEEK DRAWER
    // =========================================================================

    function escHtml(s) {
      return String(s == null ? '' : s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
    }

    // -------------------------------------------------------------------------
    // 1. LOGICAL SPACE MINI-SIMULATOR IN PROP 1 (1.12 & 1.21)
    // -------------------------------------------------------------------------
    const lsFacts = [true, false, true];
    const lsLabels = [
      'S₁: Βρέχει στην Αθήνα',
      'S₂: Το βιβλίο είναι στο τραπέζι',
      'S₃: Ο Σωκράτης είναι σοφός'
    ];

    function toggleLogicalSpaceFact(idx) {
      lsFacts[idx] = !lsFacts[idx];
      for (let i = 0; i < 3; i++) {
        const btn = document.getElementById('ls-btn-' + i);
        if (!btn) continue;
        btn.classList.toggle('hw-btn-active', lsFacts[i]);
        btn.textContent = lsLabels[i] + (lsFacts[i] ? ' [Ισχύει]' : ' [Δεν ισχύει]');
      }
      const pos = [], neg = [], real = [];
      for (let i = 0; i < 3; i++) {
        if (lsFacts[i]) {
          pos.push('S' + (i + 1));
          real.push('+S' + (i + 1));
        } else {
          neg.push('S' + (i + 1));
          real.push('−S' + (i + 1));
        }
      }
      const out = document.getElementById('ls-output');
      if (out) {
        out.textContent =
          'Κόσμος (2.04 — θετικά γεγονότα): {' + (pos.join(', ') || '∅') + '} | ' +
          'Πραγματικότητα (2.06): ' + real.join(', ') + ' | ' +
          'Μη-υπάρχοντα (1.12): {' + (neg.join(', ') || 'Κανένα') + '}';
      }
    }

    // -------------------------------------------------------------------------
    // 2. TREE VIEW (ΔΕΝΔΡΟΕΙΔΗΣ ΜΟΡΦΗ) & UNIFIED QUICK-PEEK DRAWER
    // -------------------------------------------------------------------------
    const TLP_BY_NUM = {};
    TLP_TREE_DATA.forEach(item => { TLP_BY_NUM[item.num] = item; });

    const TERMS_BY_ID = {};
    TLP_TERMS_DATA.forEach(term => { TERMS_BY_ID[term.id] = term; });

    function quickFilterTreeRoot(rootVal) {
      const sel = document.getElementById('treeRootFilter');
      if (sel) sel.value = rootVal;
      renderTreeExplorer();
    }

    function resetTreeFilters() {
      const inp = document.getElementById('treeSearchInput');
      const rootSel = document.getElementById('treeRootFilter');
      const lvlSel = document.getElementById('treeLevelFilter');
      if (inp) inp.value = '';
      if (rootSel) rootSel.value = 'all';
      if (lvlSel) lvlSel.value = 'all';
      renderTreeExplorer();
    }

    function treeRoleLabel(item) {
      if (item.kind === 'group') {
        return item.zero ? 'Ομάδα προκαταρκτικών (n.0x)' : 'Ομάδα προτάσεων';
      }
      if (item.depth === 0) return 'Κύρια πρόταση';
      if (item.zero) return 'Προκαταρκτική (n.0x)';
      if (item.depth === 1) return 'Κύριος κλάδος';
      return 'Υπο-πρόταση (βάθος ' + item.depth + ')';
    }

    function treeNodeClass(item) {
      if (item.kind === 'group') return 'tree-node tree-node-group';
      if (item.depth === 0) return 'tree-node tree-node-root';
      if (item.zero) return 'tree-node tree-node-prelim';
      if (item.depth === 1) return 'tree-node tree-node-branch';
      return 'tree-node tree-node-sub';
    }

    function renderMathText(str) {
      // Escape HTML while turning inline $...$ LaTeX segments into <span class="tex">...</span>
      const raw = String(str || '');
      if (!raw.includes('$')) return escHtml(raw);
      return raw.split(/(\$[^$]+\$)/g).map(part => {
        if (part.length > 2 && part.startsWith('$') && part.endsWith('$')) {
          return '<span class="tex">' + escHtml(part.slice(1, -1)) + '</span>';
        }
        return escHtml(part);
      }).join('');
    }

    function renderTreeExplorer(highlightNum = null) {
      const container = document.getElementById('treeExplorerContainer');
      const countBadge = document.getElementById('treeCountBadge');
      if (!container) return;

      const rawQuery = (document.getElementById('treeSearchInput')?.value || '').trim();
      const query = normSearch(rawQuery);
      const rootFilter = document.getElementById('treeRootFilter')?.value || 'all';
      const levelFilter = document.getElementById('treeLevelFilter')?.value || 'all';

      ['all', '1', '2', '3', '4', '5', '6', '7'].forEach(r => {
        const pill = document.getElementById('tree-pill-' + r);
        if (pill) pill.classList.toggle('hw-btn-active', r === rootFilter);
      });

      const filtered = TLP_TREE_DATA.filter(item => {
        if (rootFilter !== 'all' && item.root !== rootFilter) return false;
        if (levelFilter === 'roots' && !(item.kind !== 'group' && item.depth === 0)) return false;
        if (levelFilter === 'main' && !(item.kind !== 'group' && item.depth <= 1 && !item.zero)) return false;
        if (levelFilter === 'zero' && !item.zero) return false;
        if (levelFilter === 'single' && item.kind === 'group') return false;
        if (levelFilter === 'group' && item.kind !== 'group') return false;
        if (query) {
          const hay = normSearch([
            item.num, item.title || '', item.el || '', item.ogden || '',
            item.pm || '', item.de || '', item.note || ''
          ].join(' ').replace(/\$/g, ''));
          return hay.includes(query);
        }
        return true;
      });

      if (countBadge) {
        countBadge.textContent = filtered.length + ' / ' + TLP_TREE_DATA.length + ' κόμβοι';
      }

      if (filtered.length === 0) {
        container.innerHTML = '<div class="lab-empty">Δεν βρέθηκαν κόμβοι με αυτά τα κριτήρια.</div>';
        return;
      }

      const isNarrow = window.innerWidth < 640;
      container.innerHTML = filtered.map(item => {
        const effDepth = Math.min(item.depth, 4);
        const indentPx = isNarrow ? Math.min(effDepth * 8, 20) : effDepth * 22;
        const isHi = highlightNum && item.num === highlightNum;
        const nodeId = 'tree-node-' + item.num.replace(/[^0-9a-zA-Z]+/g, '-');
        const jumpBtn = item.anchor
          ? `<button type="button" class="hw-btn tree-jump-btn" onclick="jumpToAnalysisAnchor('${escHtml(item.anchor)}')">Στην ανάλυση →</button>`
          : '';

        let bodyHtml = '';
        if (item.kind === 'group') {
          bodyHtml = `
            <div class="tree-group-body">
              ${item.title ? `<div class="tree-group-title">${renderMathText(item.title)}</div>` : ''}
              <p class="tree-group-summary">${renderMathText(item.el || item.note || '')}</p>
            </div>
          `;
        } else {
          const cols = [];
          cols.push(`
            <div class="tree-col tree-col-el">
              <div class="tree-col-label">Ελληνικά</div>
              <div class="tree-col-text tree-col-primary">${renderMathText(item.el)}</div>
            </div>
          `);
          if (item.ogden) {
            cols.push(`
              <div class="tree-col">
                <div class="tree-col-label">Ogden &amp; Ramsey (1922)</div>
                <div class="tree-col-text">${renderMathText(item.ogden)}</div>
              </div>
            `);
          }
          if (item.pm) {
            cols.push(`
              <div class="tree-col">
                <div class="tree-col-label">Pears &amp; McGuinness (1961)</div>
                <div class="tree-col-text">${renderMathText(item.pm)}</div>
              </div>
            `);
          }
          if (item.de) {
            cols.push(`
              <div class="tree-col">
                <div class="tree-col-label">Γερμανικό πρωτότυπο (1921)</div>
                <div class="tree-col-text tree-col-de">${renderMathText(item.de)}</div>
              </div>
            `);
          }
          bodyHtml = `<div class="tree-cols tree-cols-${cols.length}">${cols.join('')}</div>`;
          if (item.note) {
            bodyHtml += `<div class="tree-note"><strong>Σημείωση:</strong> ${renderMathText(item.note)}</div>`;
          }
        }

        return `
          <div id="${nodeId}" class="${treeNodeClass(item)}${isHi ? ' is-highlighted' : ''}" style="--tree-indent: ${indentPx}px;">
            <div class="tree-node-head">
              <div class="tree-node-id">
                <span class="tree-num">${escHtml(item.num)}</span>
                <span class="hw-badge">${treeRoleLabel(item)}</span>
              </div>
              <div class="tree-node-actions">
                <span class="tree-root-tag">Κορμός ${escHtml(item.root)}</span>
                ${jumpBtn}
              </div>
            </div>
            ${bodyHtml}
          </div>
        `;
      }).join('');
      if (typeof renderMathIn === 'function') renderMathIn(container);
    }

    function openPropPeek(num) {
      const item = TLP_BY_NUM[num];
      if (!item) return;
      const drawer = document.getElementById('peekDrawer');
      const titleBadge = document.getElementById('peekTitleBadge');
      const subBadge = document.getElementById('peekSubBadge');
      const body = document.getElementById('peekBody');
      const btn1 = document.getElementById('peekActionPrimary');
      const btn2 = document.getElementById('peekActionSecondary');
      if (!drawer || !body) return;

      titleBadge.textContent = item.num;
      titleBadge.className = 'peek-badge-main';
      subBadge.textContent = treeRoleLabel(item);

      const blocks = [];
      if (item.el) {
        blocks.push(`
          <div class="peek-card peek-card-primary">
            <div class="peek-label">Ελληνική απόδοση</div>
            <div class="peek-text-main">${renderMathText(item.el)}</div>
          </div>
        `);
      }
      if (item.ogden) {
        blocks.push(`
          <div class="peek-card">
            <div class="peek-label">Ogden &amp; Ramsey (1922)</div>
            <div class="peek-text">${renderMathText(item.ogden)}</div>
          </div>
        `);
      }
      if (item.pm) {
        blocks.push(`
          <div class="peek-card">
            <div class="peek-label">Pears &amp; McGuinness (1961)</div>
            <div class="peek-text">${renderMathText(item.pm)}</div>
          </div>
        `);
      }
      if (item.de) {
        blocks.push(`
          <div class="peek-card">
            <div class="peek-label">Γερμανικό πρωτότυπο (1921)</div>
            <div class="peek-text peek-de">${renderMathText(item.de)}</div>
          </div>
        `);
      }
      if (item.note) {
        blocks.push(`
          <div class="peek-note">
            <strong>Σημείωση:</strong> ${renderMathText(item.note)}
          </div>
        `);
      }
      body.innerHTML = blocks.join('');
      if (typeof renderMathIn === 'function') renderMathIn(body);

      if (item.anchor) {
        btn1.hidden = false;
        btn1.textContent = 'Μετάβαση στην ανάλυση →';
        btn1.onclick = () => {
          closePeek();
          jumpToAnalysisAnchor(item.anchor);
        };
      } else {
        btn1.hidden = true;
      }

      btn2.hidden = false;
      btn2.textContent = 'Προβολή στη δενδροειδή μορφή';
      btn2.onclick = () => {
        closePeek();
        const inp = document.getElementById('treeSearchInput');
        const rootSel = document.getElementById('treeRootFilter');
        const lvlSel = document.getElementById('treeLevelFilter');
        if (inp) inp.value = '';
        if (rootSel) rootSel.value = item.root;
        if (lvlSel) lvlSel.value = 'all';
        switchMainTab('tree', true);
        renderTreeExplorer(item.num);
        setTimeout(() => {
          const el = document.getElementById('tree-node-' + item.num.replace(/[^0-9a-zA-Z]+/g, '-'));
          if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 60);
      };

      drawer.hidden = false;
    }

    function openTermPeek(termId) {
      const term = TERMS_BY_ID[termId];
      if (!term) return;
      const drawer = document.getElementById('peekDrawer');
      const titleBadge = document.getElementById('peekTitleBadge');
      const subBadge = document.getElementById('peekSubBadge');
      const body = document.getElementById('peekBody');
      const btn1 = document.getElementById('peekActionPrimary');
      const btn2 = document.getElementById('peekActionSecondary');
      if (!drawer || !body) return;

      titleBadge.textContent = term.term;
      titleBadge.className = 'peek-badge-main peek-badge-term';
      subBadge.textContent = 'Όρος του Tractatus';

      const rows = [];
      rows.push(`
        <div class="peek-card peek-card-primary">
          <div class="peek-label">Ελληνική απόδοση στην ανάλυση</div>
          <div class="peek-text-main">${escHtml(term.greek)}</div>
        </div>
      `);
      if (term.kitsopoulos) {
        rows.push(`
          <div class="peek-card">
            <div class="peek-label">Μετάφραση Θ. Κιτσόπουλου (1978)</div>
            <div class="peek-text">${escHtml(term.kitsopoulos)}</div>
          </div>
        `);
      }
      if (term.ogden || term.pm) {
        rows.push(`
          <div class="peek-card">
            <div class="peek-label">Αγγλικές μεταφράσεις</div>
            <div class="peek-text">
              ${term.ogden ? `<div><strong>Ogden (1922):</strong> ${escHtml(term.ogden)}</div>` : ''}
              ${term.pm ? `<div><strong>Pears &amp; McGuinness (1961):</strong> ${escHtml(term.pm)}</div>` : ''}
            </div>
          </div>
        `);
      }
      rows.push(`
        <div class="peek-note peek-note-prose">
          <strong>Ορισμός και ρόλος στο έργο:</strong> ${escHtml(term.definition)}
        </div>
      `);
      body.innerHTML = rows.join('');

      if (term.target) {
        btn1.hidden = false;
        btn1.textContent = (term.targetLabel || 'Μετάβαση στην ανάλυση') + ' →';
        btn1.onclick = () => {
          closePeek();
          jumpToAnalysisAnchor(term.target);
        };
      } else {
        btn1.hidden = true;
      }
      btn2.hidden = true;
      drawer.hidden = false;
    }

    function closePeek() {
      const drawer = document.getElementById('peekDrawer');
      if (drawer) drawer.hidden = true;
    }

    function bindInteractiveRefs() {
      document.querySelectorAll('#masterContentContainer .prop-ref').forEach(el => {
        const num = el.dataset.prop || (el.textContent.match(/\b([1-7](?:\.\d+)?)\b/) || [])[1];
        if (!num || !TLP_BY_NUM[num]) return;
        el.classList.add('is-clickable');
        el.title = 'Προβολή πρότασης ' + num;
        el.setAttribute('role', 'button');
        el.setAttribute('tabindex', '0');
        el.addEventListener('click', (e) => { e.preventDefault(); openPropPeek(num); });
        el.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openPropPeek(num); }
        });
      });

      document.querySelectorAll('#masterContentContainer .term-ref').forEach(el => {
        const tid = el.dataset.term;
        if (!tid || !TERMS_BY_ID[tid]) return;
        el.title = 'Όρος: ' + TERMS_BY_ID[tid].term + ' — κλικ για ορισμό και ανάλυση';
        el.setAttribute('role', 'button');
        el.setAttribute('tabindex', '0');
        el.addEventListener('click', (e) => { e.preventDefault(); openTermPeek(tid); });
        el.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openTermPeek(tid); }
        });
      });
    }

    // -------------------------------------------------------------------------
    // 3. LOGIC LAB: TRUTH TABLES (5.101), W-p-F DIAGRAM (6.1203), URN (5.154)
    // -------------------------------------------------------------------------
    let ttCells = [1, 1, 0, 1];

    const TT_CATALOG_5101 = {
      'WWWW': { idx: 1, sym: '⊤ (Ταυτολογία)', short: '⊤', verbal: '«Αν p, τότε p· και αν q, τότε q.»', nForm: 'N(N(p, N(p)), N(q, N(q)))', status: 'Ταυτολογία (sinnlos — άνευ όρων αληθής)', comment: 'Ακραία οριακή περίπτωση (4.46): επιτρέπει ολόκληρο τον λογικό χώρο. Δεν λέει τίποτα για τον κόσμο, αλλά δείχνει τη λογική δομή.' },
      'FWWW': { idx: 2, sym: '¬(p ∧ q) (NAND)', short: '¬(p∧q)', verbal: '«Όχι και τα δύο, p και q.» (~(p · q))', nForm: 'N(N(N(p), N(q)))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αποκλείει μόνο τον συνδυασμό όπου p και q είναι ταυτόχρονα αληθή (βάσεις αληθείας: Wᵣ = 3).' },
      'WFWW': { idx: 3, sym: 'q ⊃ p', short: 'q⊃p', verbal: '«Αν q, τότε p.»', nForm: 'N(N(N(q), p))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αντίστροφη συνεπαγωγή: ψευδής μόνο όταν το q είναι αληθές και το p ψευδές (Wᵣ = 3).' },
      'WWFW': { idx: 4, sym: 'p ⊃ q (Συνεπαγωγή)', short: 'p⊃q', verbal: '«Αν p, τότε q.»', nForm: 'N(N(N(p), q))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Υλική συνεπαγωγή: ψευδής μόνο στην 3η γραμμή (όταν p=W και q=F). Βάσεις αληθείας: Wᵣ = 3.' },
      'WWWF': { idx: 5, sym: 'p ∨ q (Διάζευξη)', short: 'p∨q', verbal: '«p ή q.»', nForm: 'N(N(p, q))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αληθής αν τουλάχιστον μία από τις p, q είναι αληθής. Είναι η άρνηση της κοινής άρνησης N(p, q).' },
      'FFWW': { idx: 6, sym: '¬q', short: '¬q', verbal: '«Όχι q.» (~q)', nForm: 'N(q)', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Άρνηση της στοιχειώδους πρότασης q (Wᵣ = 2).' },
      'FWFW': { idx: 7, sym: '¬p', short: '¬p', verbal: '«Όχι p.» (~p)', nForm: 'N(p)', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Άρνηση της στοιχειώδους πρότασης p (Wᵣ = 2).' },
      'FWWF': { idx: 8, sym: 'p ≢ q (XOR)', short: 'p⊕q', verbal: '«p ή q, αλλά όχι και τα δύο.»', nForm: 'N(N(p, q), N(N(p), N(q)))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αληθής όταν οι p και q έχουν αντίθετες τιμές αληθείας (Wᵣ = 2).' },
      'WFFW': { idx: 9, sym: 'p ≡ q (Ισοδυναμία)', short: 'p≡q', verbal: '«Αν p, τότε q· και αν q, τότε p.»', nForm: 'N(N(N(p, q), N(N(p), N(q))))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αληθής όταν οι p και q έχουν την ίδια τιμή αληθείας (Wᵣ = 2).' },
      'WFWF': { idx: 10, sym: 'p', short: 'p', verbal: '«p» (Κατάφαση της p)', nForm: 'N(N(p)) = p', status: 'Στοιχειώδης πρόταση (sinnvoll)', comment: 'Η στοιχειώδης πρόταση p ως συνάρτηση αληθείας του εαυτού της (Πρόταση 5).' },
      'WWFF': { idx: 11, sym: 'q', short: 'q', verbal: '«q» (Κατάφαση της q)', nForm: 'N(N(q)) = q', status: 'Στοιχειώδης πρόταση (sinnvoll)', comment: 'Η στοιχειώδης πρόταση q ως συνάρτηση αληθείας του εαυτού της (Πρόταση 5).' },
      'FFFW': { idx: 12, sym: 'N(p, q) = ¬p ∧ ¬q (NOR)', short: 'N(p,q)', verbal: '«Ούτε p ούτε q.» (~p · ~q)', nForm: 'N(p, q)', status: 'Τελεστής κοινής άρνησης N(p, q)', comment: 'Η θεμελιώδης πράξη του Tractatus (5.5 & 6): αληθής μόνο όταν και η p και η q είναι ψευδείς.' },
      'FFWF': { idx: 13, sym: 'p ∧ ¬q', short: 'p∧¬q', verbal: '«p και όχι q.»', nForm: 'N(N(p), q)', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αληθής μόνο στην 3η γραμμή (όταν p=W και q=F, Wᵣ = 1).' },
      'FWFF': { idx: 14, sym: 'q ∧ ¬p', short: 'q∧¬p', verbal: '«q και όχι p.»', nForm: 'N(p, N(q))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αληθής μόνο στη 2η γραμμή (όταν p=F και q=W, Wᵣ = 1).' },
      'WFFF': { idx: 15, sym: 'p ∧ q (Σύζευξη)', short: 'p∧q', verbal: '«p και q.» (p · q)', nForm: 'N(N(p), N(q))', status: 'Πρόταση με νόημα (sinnvoll)', comment: 'Αληθής μόνο στην 1η γραμμή (όταν και η p και η q είναι αληθείς, Wᵣ = 1).' },
      'FFFF': { idx: 16, sym: '⊥ (Αντίφαση)', short: '⊥', verbal: '«p και όχι p· και q και όχι q.»', nForm: 'N(N(p, N(p)))', status: 'Αντίφαση (sinnlos — άνευ όρων ψευδής)', comment: 'Ακραία οριακή περίπτωση (4.46): δεν επιτρέπει κανένα σημείο στον λογικό χώρο (Wᵣ = 0).' }
    };

    function keyToArr(key) { return key.split('').map(c => c === 'W' ? 1 : 0); }

    function render16Matrix() {
      const box = document.getElementById('tt16Matrix');
      if (!box) return;
      const activeKey = ttCells.map(v => v === 1 ? 'W' : 'F').join('');
      box.innerHTML = Object.entries(TT_CATALOG_5101).map(([key, info]) => {
        const isActive = key === activeKey;
        return `
          <button type="button" onclick="setTruthTablePreset(keyToArr('${key}'))"
            class="hw-btn tt-matrix-btn${isActive ? ' hw-btn-active' : ''}">
            <span class="tt-matrix-sym">#${info.idx} ${info.short}</span>
            <span class="tt-matrix-key">(${key})</span>
          </button>
        `;
      }).join('');
    }

    function populateProbabilitySelects() {
      const rSel = document.getElementById('probSelectR');
      const sSel = document.getElementById('probSelectS');
      if (!rSel || !sSel || rSel.options.length > 0) return;
      Object.entries(TT_CATALOG_5101).forEach(([key, info]) => {
        const val = key.split('').map(c => c === 'W' ? 1 : 0).join(',');
        const wr = key.split('').filter(c => c === 'W').length;
        const label = `#${info.idx} ${info.short} (${key} — W=${wr})`;
        rSel.add(new Option(label, val, false, key === 'WWWF'));
        sSel.add(new Option(label, val, false, key === 'WFFF'));
      });
    }

    function syncProbSFromLab2A() {
      populateProbabilitySelects();
      const sSel = document.getElementById('probSelectS');
      if (!sSel) return;
      sSel.value = ttCells.join(',');
      calculateLogicalProbability();
    }

    function toggleTruthCell(idx) {
      ttCells[idx] = ttCells[idx] === 1 ? 0 : 1;
      updateTruthTableDiagnosis();
    }

    function setTruthTablePreset(arr) {
      ttCells = arr.slice();
      updateTruthTableDiagnosis();
    }

    function updateTruthTableDiagnosis() {
      const key = ttCells.map(v => v === 1 ? 'W' : 'F').join('');
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('tt-cell-' + i);
        if (!btn) continue;
        const isW = ttCells[i] === 1;
        btn.textContent = isW ? 'W' : 'F';
        btn.classList.toggle('tt-btn-w', isW);
        btn.classList.toggle('tt-btn-f', !isW);
      }
      document.querySelectorAll('.tt-preset-btn').forEach(btn => {
        btn.classList.toggle('hw-btn-active', btn.dataset.preset === key);
      });
      const info = TT_CATALOG_5101[key];
      if (info) {
        document.getElementById('tt-witt-sign').textContent = '(' + key + ')(p, q)';
        document.getElementById('tt-sym-name').textContent = '#' + info.idx + ': ' + info.sym;
        document.getElementById('tt-verbal-desc').textContent = info.verbal;
        document.getElementById('tt-n-formula').textContent = 'Παραγωγή με N(ξ̄): ' + info.nForm;
        document.getElementById('tt-status-badge').textContent = info.status;
        document.getElementById('tt-phil-comment').textContent = info.comment;
      }
      render16Matrix();
    }

    let currentWpfMode = 'noncontra';
    function renderWpfDiagram(mode) {
      currentWpfMode = mode;
      ['notp', 'noncontra', 'exclmid'].forEach(m => {
        const b = document.getElementById('wpf-btn-' + m);
        if (b) b.classList.toggle('hw-btn-active', m === mode);
      });
      const svgBox = document.getElementById('wpfSvgContainer');
      const expBox = document.getElementById('wpfExplanation');
      if (!svgBox || !expBox) return;

      if (mode === 'notp') {
        svgBox.innerHTML = `
          <svg viewBox="0 0 420 175" class="lab-svg" style="max-width:420px">
            <rect x="130" y="18" width="160" height="36" fill="none" stroke="currentColor" stroke-width="1.5"/>
            <text x="155" y="41" fill="currentColor" font-size="14" font-weight="bold">W</text>
            <text x="210" y="41" fill="currentColor" font-size="14" font-weight="bold">p</text>
            <text x="265" y="41" fill="currentColor" font-size="14" font-weight="bold">F</text>
            <line x1="160" y1="54" x2="265" y2="118" stroke="var(--muted-foreground)" stroke-width="2" stroke-dasharray="5,4"/>
            <line x1="265" y1="54" x2="160" y2="118" stroke="var(--primary)" stroke-width="2.5"/>
            <rect x="130" y="118" width="160" height="36" fill="none" stroke="currentColor" stroke-width="2"/>
            <text x="145" y="141" fill="var(--primary)" font-size="14" font-weight="bold">W(~p)</text>
            <text x="242" y="141" fill="currentColor" font-size="14" font-weight="bold">F(~p)</text>
          </svg>
        `;
        expBox.innerHTML = '<strong>Άρνηση ~p (6.1203):</strong> Οι πόλοι αντιστρέφονται: ο εξωτερικός πόλος <strong>W(~p)</strong> συνδέεται με το εσωτερικό <strong>F</strong> του p, και ο εξωτερικός πόλος <strong>F(~p)</strong> με το εσωτερικό <strong>W</strong> του p. Η πρόταση είναι <strong>διπολική (sinnvoll)</strong>.';
      } else if (mode === 'noncontra') {
        svgBox.innerHTML = `
          <svg viewBox="0 0 480 205" class="lab-svg" style="max-width:480px">
            <text x="240" y="22" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold">ΕΣΩΤΕΡΙΚΟΙ ΠΟΛΟΙ: W — p — F</text>
            <rect x="140" y="32" width="200" height="34" fill="none" stroke="currentColor" stroke-width="1.5"/>
            <text x="165" y="54" fill="currentColor" font-size="14" font-weight="bold">W</text>
            <text x="240" y="54" fill="currentColor" font-size="14" font-weight="bold">p</text>
            <text x="310" y="54" fill="currentColor" font-size="14" font-weight="bold">F</text>
            <path d="M 170 66 C 170 115, 160 120, 160 145" fill="none" stroke="var(--primary)" stroke-width="2.5"/>
            <path d="M 315 66 C 315 115, 180 120, 175 145" fill="none" stroke="var(--primary)" stroke-width="2.5"/>
            <rect x="105" y="145" width="130" height="38" fill="var(--truth-bg)" stroke="var(--primary)" stroke-width="2.5"/>
            <text x="170" y="169" text-anchor="middle" fill="var(--primary)" font-size="13" font-weight="bold">W (ΟΛΑ ΕΔΩ)</text>
            <rect x="270" y="145" width="125" height="38" fill="none" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="4,4"/>
            <text x="332" y="169" text-anchor="middle" fill="var(--muted-foreground)" font-size="13">F (ΚΕΝΟ: 0)</text>
          </svg>
        `;
        expBox.innerHTML = '<strong>Αρχή μη αντίφασης ~(p · ~p) (6.1203):</strong> Τόσο ο πόλος <strong>W</strong> όσο και ο πόλος <strong>F</strong> του p καταλήγουν στον εξωτερικό πόλο <strong>W</strong>, ενώ στον <strong>F</strong> δεν καταλήγει καμία γραμμή. Βλέπουμε <em>από το σύμβολο και μόνο</em> (6.113) ότι είναι <strong>ταυτολογία</strong>.';
      } else {
        svgBox.innerHTML = `
          <svg viewBox="0 0 480 205" class="lab-svg" style="max-width:480px">
            <text x="240" y="22" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold">ΑΡΧΗ ΤΡΙΤΟΥ ΑΠΟΚΛΕΙΟΜΕΝΟΥ: p ∨ ~p</text>
            <rect x="140" y="32" width="200" height="34" fill="none" stroke="currentColor" stroke-width="1.5"/>
            <text x="165" y="54" fill="currentColor" font-size="14" font-weight="bold">W</text>
            <text x="240" y="54" fill="currentColor" font-size="14" font-weight="bold">p</text>
            <text x="310" y="54" fill="currentColor" font-size="14" font-weight="bold">F</text>
            <path d="M 170 66 L 165 145" fill="none" stroke="var(--primary)" stroke-width="2.5"/>
            <path d="M 315 66 C 315 105, 190 110, 180 145" fill="none" stroke="var(--primary)" stroke-width="2.5"/>
            <rect x="105" y="145" width="130" height="38" fill="var(--truth-bg)" stroke="var(--primary)" stroke-width="2.5"/>
            <text x="170" y="169" text-anchor="middle" fill="var(--primary)" font-size="14" font-weight="bold">W (100%)</text>
            <rect x="270" y="145" width="125" height="38" fill="none" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="4,4"/>
            <text x="332" y="169" text-anchor="middle" fill="var(--muted-foreground)" font-size="13">F (ΚΕΝΟ: 0)</text>
          </svg>
        `;
        expBox.innerHTML = '<strong>p ∨ ~p («Βρέχει ή δεν βρέχει», 4.461):</strong> Είτε το p είναι W είτε είναι F, η αγκύλη οδηγεί πάντα στον εξωτερικό πόλο <strong>W</strong>. Η ταυτολογία επιτρέπει κάθε δυνατή κατάσταση πραγμάτων, άρα δεν λέει τίποτα για τον καιρό.';
      }
    }

    function calculateLogicalProbability() {
      populateProbabilitySelects();
      const rSel = document.getElementById('probSelectR');
      const sSel = document.getElementById('probSelectS');
      const box = document.getElementById('probResultBox');
      const urnBox = document.getElementById('probUrnSvg');
      if (!rSel || !sSel || !box) return;

      const rArr = rSel.value.split(',').map(Number);
      const sArr = sSel.value.split(',').map(Number);
      let Wr = 0, Wrs = 0;
      const rows = ['(WW)', '(FW)', '(WF)', '(FF)'];
      const rowDetails = [];
      const urnBalls = [];

      for (let i = 0; i < 4; i++) {
        if (rArr[i] === 1) {
          Wr++;
          if (sArr[i] === 1) {
            Wrs++;
            rowDetails.push(rows[i] + ': r=W & s=W [✓ Κοινή]');
            urnBalls.push({ label: rows[i], hit: true });
          } else {
            rowDetails.push(rows[i] + ': r=W & s=F [✕ Μόνο r]');
            urnBalls.push({ label: rows[i], hit: false });
          }
        }
      }

      if (urnBox) {
        if (Wr === 0) {
          urnBox.innerHTML = '<span class="lab-note">Η πρόταση-βάση r είναι αντίφαση (Wᵣ = 0) — κενή κάλπη.</span>';
        } else {
          const ballsSvg = urnBalls.map((b, idx) => {
            const cx = 140 + idx * 54 - ((urnBalls.length - 1) * 27);
            return `
              <circle cx="${cx}" cy="48" r="18" fill="${b.hit ? 'var(--primary)' : 'var(--card)'}" stroke="currentColor" stroke-width="2"/>
              <text x="${cx}" y="52" text-anchor="middle" fill="${b.hit ? 'var(--primary-foreground)' : 'currentColor'}" font-size="10" font-weight="bold">${b.label}</text>
            `;
          }).join('');
          urnBox.innerHTML = `
            <svg viewBox="0 0 280 96" class="lab-svg" style="max-width:280px">
              <path d="M 35 16 L 55 82 L 225 82 L 245 16" fill="none" stroke="currentColor" stroke-width="2"/>
              <text x="140" y="14" text-anchor="middle" fill="var(--muted-foreground)" font-size="10">ΚΑΛΠΗ 5.154 (Wᵣ = ${Wr} δυνατές βάσεις)</text>
              ${ballsSvg}
            </svg>
          `;
        }
      }

      const probStr = Wr === 0 ? 'Απροσδιόριστη (0/0)' : `${Wrs} / ${Wr} = ${(Wrs / Wr * 100).toFixed(1)}%`;
      let note = '';
      if (Wr === 0) {
        note = 'Μια αντίφαση (Wᵣ = 0) δεν μπορεί να αποτελέσει βάση λογικής πιθανότητας.';
      } else if (Wrs === Wr) {
        note = 'Επειδή Wᵣₛ = Wᵣ, όλες οι βάσεις αληθείας της r είναι και βάσεις της s: άρα η s απορρέει λογικά από την r (5.11–5.12, βεβαιότητα = 1).';
      } else if (Wrs === 0) {
        note = 'Επειδή Wᵣₛ = 0, οι προτάσεις r και s αλληλοαποκλείονται (πιθανότητα = 0).';
      } else {
        note = 'Σύμφωνα με το 5.15, η r δίνει στην s τη λογική πιθανότητα Wᵣₛ : Wᵣ = ' + Wrs + '/' + Wr + '.';
      }

      box.innerHTML = `
        <div class="readout-headline">Λογική πιθανότητα P(s | r) = Wᵣₛ / Wᵣ = ${probStr}</div>
        <div>Βάσεις της r (Wᵣ = ${Wr}) | Κοινές βάσεις r και s (Wᵣₛ = ${Wrs})</div>
        <div class="muted">${rowDetails.join(' &nbsp;|&nbsp; ') || '—'}</div>
        <div class="readout-foot">${note}</div>
      `;
    }

    // -------------------------------------------------------------------------
    // 4. VISUAL MODELS: PARIS, NECKER CUBE, EYE (5.6331), GRAMOPHONE (4.014)
    // -------------------------------------------------------------------------
    function setParisScenario(scen) {
      const mSel = document.getElementById('parisModelSelect');
      const rSel = document.getElementById('parisRealitySelect');
      if (scen === 'match') { mSel.value = 'cut'; rSel.value = 'cut'; }
      else { mSel.value = 'cut'; rSel.value = 'parallel'; }
      updateParisSimulation();
    }

    function cycleParisModel() {
      const mSel = document.getElementById('parisModelSelect');
      const order = ['cut', 'parallel', 'behind'];
      mSel.value = order[(order.indexOf(mSel.value) + 1) % order.length];
      updateParisSimulation();
    }

    function updateParisSimulation() {
      const mVal = document.getElementById('parisModelSelect')?.value;
      const rVal = document.getElementById('parisRealitySelect')?.value;
      const svgContainer = document.getElementById('parisSvgContainer');
      const banner = document.getElementById('parisStatusBanner');
      if (!svgContainer || !banner) return;

      const isMatch = (mVal === rVal);
      document.getElementById('paris-scen-match').classList.toggle('hw-btn-active', isMatch);
      document.getElementById('paris-scen-mismatch').classList.toggle('hw-btn-active', !isMatch);

      const posMap = {
        cut: { x: 95, y: 105, ang: 28 },
        parallel: { x: 95, y: 68, ang: 0 },
        behind: { x: 82, y: 129, ang: 0 }
      };
      const mp = posMap[mVal] || posMap.cut;
      const rp = posMap[rVal] || posMap.cut;
      const feelerColor = isMatch ? 'var(--primary)' : 'var(--muted-foreground)';

      svgContainer.innerHTML = `
        <svg viewBox="0 0 680 238" class="lab-svg" style="max-width:680px">
          <text x="340" y="18" text-anchor="middle" fill="var(--primary)" font-size="11.5" font-weight="bold">Κεραίες (Fühler 2.1515): a' ⟷ a</text>
          <rect x="15" y="34" width="270" height="172" fill="var(--card)" stroke="currentColor" stroke-width="2"/>
          <text x="150" y="54" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">ΤΡΑΠΕΖΙ ΔΙΚΑΣΤΗΡΙΟΥ (ΕΙΚΟΝΑ)</text>
          <text x="150" y="68" text-anchor="middle" fill="var(--muted-foreground)" font-size="10">(Κλικ στο a' για αλλαγή θέσης)</text>
          <g transform="translate(${mp.x}, ${mp.y + 14}) rotate(${mp.ang})" onclick="cycleParisModel()" style="cursor:pointer;">
            <rect x="-28" y="-14" width="56" height="28" fill="var(--primary)" fill-opacity="0.22" stroke="var(--primary)" stroke-width="2.2"/>
            <text x="0" y="4" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">a' (Αυτ.)</text>
          </g>
          <rect x="155" y="129" width="60" height="28" fill="none" stroke="currentColor" stroke-width="2"/>
          <text x="185" y="147" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">b' (Καρ.)</text>

          <rect x="395" y="34" width="270" height="172" fill="var(--card)" stroke="currentColor" stroke-width="2"/>
          <text x="530" y="54" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">ΔΡΟΜΟΣ ΠΑΡΙΣΙΟΥ (ΠΡΑΓΜΑΤΙΚΟΤΗΤΑ)</text>
          <g transform="translate(${380 + rp.x}, ${rp.y + 14}) rotate(${rp.ang})">
            <rect x="-28" y="-14" width="56" height="28" fill="currentColor" fill-opacity="0.16" stroke="currentColor" stroke-width="2"/>
            <text x="0" y="4" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">a (Αυτ.)</text>
          </g>
          <rect x="535" y="129" width="60" height="28" fill="none" stroke="currentColor" stroke-width="2"/>
          <text x="565" y="147" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">b (Καρ.)</text>

          <path d="M ${mp.x} ${mp.y} C 220 26, 460 26, ${380 + rp.x} ${rp.y}" fill="none" stroke="${feelerColor}" stroke-width="1.8" stroke-dasharray="5,4"/>
          <path d="M 215 143 C 310 212, 430 212, 535 143" fill="none" stroke="${feelerColor}" stroke-width="1.8" stroke-dasharray="5,4"/>
          <text x="340" y="228" text-anchor="middle" fill="var(--primary)" font-size="11.5" font-weight="bold">Bedeutung (3.203): b' ⟷ b</text>
        </svg>
      `;

      const sinnDesc = {
        cut: '«Το αυτοκίνητο a έκοψε τον δρόμο στο καρότσι b»',
        parallel: '«Το αυτοκίνητο a κινήθηκε παράλληλα με το καρότσι b»',
        behind: '«Το αυτοκίνητο a ακολουθούσε πίσω από το καρότσι b»'
      }[mVal];

      if (isMatch) {
        banner.innerHTML = `<strong class="accent-text">[Αληθής εικόνα — Wahr (2.222)]</strong> | <strong>Νόημα (Sinn 2.221):</strong> ${sinnDesc} | Η δομή της μακέτας συμφωνεί με την πραγματική διαμόρφωση των αντικειμένων a, b στον δρόμο.`;
      } else {
        banner.innerHTML = `<strong class="accent-text">[Ψευδής εικόνα — Falsch, με πλήρες νόημα (2.22 &amp; 3.24)]</strong> | <strong>Νόημα (Sinn):</strong> ${sinnDesc} | Παρότι στον δρόμο δεν έγινε έτσι, η εικόνα παραμένει κατανοητή διότι τα απλά ονόματα a', b' αγγίζουν τα υπαρκτά αντικείμενα a, b.`;
      }
    }

    let currentNeckerMode = 'a-front';
    function setNeckerMode(mode) {
      currentNeckerMode = mode;
      const map = { 'a': 'a-front', 'b': 'b-front', 'n': 'neutral' };
      ['a', 'b', 'n'].forEach(k => {
        const btn = document.getElementById('necker-btn-' + k);
        if (btn) btn.classList.toggle('hw-btn-active', map[k] === mode);
      });
      const svgBox = document.getElementById('neckerSvgContainer');
      const cap = document.getElementById('neckerCaption');
      if (!svgBox || !cap) return;

      const aStroke = mode === 'a-front' ? '3.5' : (mode === 'b-front' ? '1.3' : '2');
      const bStroke = mode === 'b-front' ? '3.5' : (mode === 'a-front' ? '1.3' : '2');
      const aDash = mode === 'b-front' ? '4,4' : 'none';
      const bDash = mode === 'a-front' ? '4,4' : 'none';
      const aCol = mode === 'a-front' ? 'var(--primary)' : 'currentColor';
      const bCol = mode === 'b-front' ? 'var(--primary)' : 'currentColor';

      svgBox.innerHTML = `
        <svg viewBox="0 0 340 225" class="lab-svg" style="max-width:270px">
          <rect x="65" y="75" width="120" height="110" onclick="setNeckerMode('a-front')" style="cursor:pointer;"
            fill="${mode === 'a-front' ? 'var(--primary)' : 'transparent'}" fill-opacity="0.12"
            stroke="${aCol}" stroke-width="${aStroke}" stroke-dasharray="${aDash}"/>
          <rect x="110" y="30" width="120" height="110" onclick="setNeckerMode('b-front')" style="cursor:pointer;"
            fill="${mode === 'b-front' ? 'var(--primary)' : 'transparent'}" fill-opacity="0.12"
            stroke="${bCol}" stroke-width="${bStroke}" stroke-dasharray="${bDash}"/>
          <line x1="110" y1="30" x2="65" y2="75" stroke="currentColor" stroke-width="1.8"/>
          <line x1="230" y1="30" x2="185" y2="75" stroke="currentColor" stroke-width="1.8"/>
          <line x1="110" y1="140" x2="65" y2="185" stroke="currentColor" stroke-width="1.8"/>
          <line x1="230" y1="140" x2="185" y2="185" stroke="currentColor" stroke-width="1.8"/>
          <text x="50" y="80" fill="${aCol}" font-size="14" font-weight="bold">a</text>
          <text x="192" y="80" fill="${aCol}" font-size="14" font-weight="bold">a</text>
          <text x="50" y="195" fill="${aCol}" font-size="14" font-weight="bold">a</text>
          <text x="192" y="195" fill="${aCol}" font-size="14" font-weight="bold">a</text>
          <text x="102" y="24" fill="${bCol}" font-size="14" font-weight="bold">b</text>
          <text x="236" y="24" fill="${bCol}" font-size="14" font-weight="bold">b</text>
          <text x="102" y="135" fill="${bCol}" font-size="14" font-weight="bold">b</text>
          <text x="236" y="135" fill="${bCol}" font-size="14" font-weight="bold">b</text>
          <text x="170" y="214" text-anchor="middle" fill="var(--muted-foreground)" font-size="10">(Κάντε κλικ στις έδρες a ή b)</text>
        </svg>
      `;

      if (mode === 'a-front') {
        cap.innerHTML = '<strong>Γεγονός 1 (Οι γωνίες a μπροστά):</strong> Βλέπουμε τον κύβο από πάνω-δεξιά. Η σκέψη προβάλλει μια συγκεκριμένη σχέση βάθους στα ίδια σημεία.';
      } else if (mode === 'b-front') {
        cap.innerHTML = '<strong>Γεγονός 2 (Οι γωνίες b μπροστά):</strong> Βλέπουμε τον κύβο από κάτω-αριστερά. Τα αντικείμενα (γραμμές) δεν άλλαξαν, αλλά αντιλαμβανόμαστε ένα <strong>δεύτερο, διαφορετικό γεγονός (5.5423)</strong>.';
      } else {
        cap.innerHTML = '<strong>Το αμφίσημο σχήμα του 5.5423:</strong> Ανάλογα με το ποιες κορυφές (a ή b) εστιάζουμε, το ίδιο σύμπλεγμα σημείων διαβάζεται ως δύο διαφορετικά γεγονότα.';
      }
    }

    let currentEyeMode = 'limit';
    function setEyeDiagramMode(mode) {
      currentEyeMode = mode;
      document.getElementById('eye-btn-flawed').classList.toggle('hw-btn-active', mode === 'flawed');
      document.getElementById('eye-btn-limit').classList.toggle('hw-btn-active', mode === 'limit');
      const svgBox = document.getElementById('eyeSvgContainer');
      const cap = document.getElementById('eyeCaption');
      if (!svgBox || !cap) return;

      if (mode === 'flawed') {
        svgBox.innerHTML = `
          <svg viewBox="0 0 420 200" class="lab-svg" style="max-width:345px">
            <path d="M 100 100 C 170 45, 380 15, 380 100 C 380 185, 170 155, 100 100 Z" fill="var(--card)" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>
            <line x1="62" y1="100" x2="96" y2="100" stroke="var(--primary)" stroke-width="2"/>
            <text x="56" y="105" text-anchor="end" fill="var(--primary)" font-size="14" font-weight="bold">Auge</text>
            <text x="56" y="122" text-anchor="end" fill="var(--primary)" font-size="11">(Μάτι)</text>
            <text x="262" y="104" text-anchor="middle" fill="currentColor" font-size="14" font-weight="bold">ΟΠΤΙΚΟ ΠΕΔΙΟ (5.6331)</text>
          </svg>
        `;
        cap.innerHTML = '<strong>✕ Το εσφαλμένο διάγραμμα του 5.6331:</strong> Ο Wittgenstein σχεδιάζει αυτό το σχήμα για να δείξει ποια μορφή <strong>δεν</strong> έχει το οπτικό πεδίο. Το μάτι σχεδιάζεται στην αιχμή του σχήματος, σαν να ήταν μέρος του περιγράμματος του πεδίου. Όμως το μάτι δεν το βλέπεις, και τίποτα μέσα στο οπτικό πεδίο δεν επιτρέπει να συμπεράνεις ότι το βλέπει ένα μάτι (5.633).';
      } else {
        svgBox.innerHTML = `
          <svg viewBox="0 0 420 200" class="lab-svg" style="max-width:345px">
            <polygon points="35,100 115,35 115,165" fill="var(--primary)" fill-opacity="0.08"/>
            <circle cx="35" cy="100" r="4.5" fill="var(--primary)"/>
            <text x="48" y="124" text-anchor="middle" fill="var(--primary)" font-size="11" font-weight="bold">Εγώ = Όριο</text>
            <text x="48" y="138" text-anchor="middle" fill="var(--primary)" font-size="10.5" font-weight="bold">(5.632)</text>
            <line x1="39" y1="98" x2="115" y2="35" stroke="var(--primary)" stroke-width="1.5" stroke-dasharray="4,4"/>
            <line x1="39" y1="102" x2="115" y2="165" stroke="var(--primary)" stroke-width="1.5" stroke-dasharray="4,4"/>
            <rect x="115" y="35" width="265" height="130" fill="var(--card)" stroke="currentColor" stroke-width="2.5"/>
            <text x="247" y="75" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold">ΚΑΘΑΡΗ ΠΡΑΓΜΑΤΙΚΟΤΗΤΑ (5.64)</text>
            <text x="247" y="105" text-anchor="middle" fill="currentColor" font-size="12">[Γεγονός Α] &nbsp; [Γεγονός Β]</text>
            <text x="247" y="135" text-anchor="middle" fill="var(--muted-foreground)" font-size="11">(Κανένα «Υποκείμενο» εντός του κόσμου)</text>
          </svg>
        `;
        cap.innerHTML = '<strong>✓ Το υποκείμενο ως αδιάστατο σημείο-όριο (5.632 &amp; 5.64):</strong> Το Εγώ συρρικνώνεται σε αδιάστατο σημείο στο όριο του κόσμου, και μέσα στο κάδρο απομένει η αντικειμενική πραγματικότητα (ο σολιψισμός ταυτίζεται με τον καθαρό ρεαλισμό).';
      }
    }

    let gramNotes = [1, 2, 3, 2];
    const GRAM_LABELS = { 1: 'Χαμηλή (1)', 2: 'Μεσαία (2)', 3: 'Υψηλή (3)' };

    function setGramophonePreset(arr, id) {
      gramNotes = arr.slice();
      document.querySelectorAll('.gram-preset-btn').forEach(b => b.classList.remove('hw-btn-active'));
      const active = document.getElementById('gram-preset-' + id);
      if (active) active.classList.add('hw-btn-active');
      renderGramophoneLab();
    }

    function cycleGramophoneNote(idx) {
      gramNotes[idx] = (gramNotes[idx] % 3) + 1;
      document.querySelectorAll('.gram-preset-btn').forEach(b => b.classList.remove('hw-btn-active'));
      renderGramophoneLab();
    }

    function renderGramophoneLab() {
      const svgBox = document.getElementById('gramophoneSvgContainer');
      const readout = document.getElementById('gramophoneReadout');
      if (!svgBox || !readout) return;

      for (let i = 0; i < 4; i++) {
        const b = document.getElementById('gram-note-btn-' + i);
        if (b) b.textContent = (i + 1) + 'η: ' + GRAM_LABELS[gramNotes[i]];
      }

      const noteY = { 1: 120, 2: 95, 3: 70 };
      const scoreNotes = gramNotes.map((n, i) => {
        const x = 55 + i * 42;
        const y = noteY[n];
        return `
          <g onclick="cycleGramophoneNote(${i})" style="cursor:pointer;">
            <circle cx="${x}" cy="${y}" r="8" fill="var(--primary)"/>
            <line x1="${x + 7}" y1="${y}" x2="${x + 7}" y2="${y - 26}" stroke="var(--primary)" stroke-width="2"/>
            <text x="${x}" y="152" text-anchor="middle" fill="currentColor" font-size="10">${n}</text>
          </g>
        `;
      }).join('');

      const grooveX = gramNotes.map((n, i) => {
        const x0 = 268 + i * 46;
        const amp = n === 1 ? -10 : (n === 2 ? 0 : 12);
        return `Q ${x0 + 11} ${95 - amp * 2.2}, ${x0 + 23} 95 T ${x0 + 46} 95`;
      }).join(' ');

      const waveBars = gramNotes.map((n, i) => {
        const x = 515 + i * 44;
        const h = n === 1 ? 18 : (n === 2 ? 36 : 56);
        return `
          <rect x="${x - 10}" y="${95 - h / 2}" width="20" height="${h}" fill="var(--primary)" fill-opacity="0.28" stroke="var(--primary)" stroke-width="1.8"/>
          <text x="${x}" y="152" text-anchor="middle" fill="currentColor" font-size="10">${n * 220}Hz</text>
        `;
      }).join('');

      svgBox.innerHTML = `
        <svg viewBox="0 0 720 175" class="lab-svg" style="min-width:540px;max-width:670px">
          <rect x="12" y="15" width="215" height="148" fill="var(--card)" stroke="currentColor" stroke-width="1.5"/>
          <text x="119" y="34" text-anchor="middle" fill="currentColor" font-size="11" font-weight="bold">1. ΠΑΡΤΙΤΟΥΡΑ (Notenschrift)</text>
          ${[65, 80, 95, 110, 125].map(y => `<line x1="26" y1="${y}" x2="212" y2="${y}" stroke="var(--border)" stroke-width="1.2"/>`).join('')}
          ${scoreNotes}

          <text x="236" y="95" text-anchor="middle" fill="var(--primary)" font-size="14" font-weight="bold">⇄</text>

          <rect x="248" y="15" width="222" height="148" fill="var(--card)" stroke="currentColor" stroke-width="1.5"/>
          <text x="359" y="34" text-anchor="middle" fill="currentColor" font-size="11" font-weight="bold">2. ΔΙΣΚΟΣ (Grammophonplatte)</text>
          <line x1="262" y1="95" x2="458" y2="95" stroke="var(--border)" stroke-dasharray="3,3"/>
          <path d="M 268 95 ${grooveX}" fill="none" stroke="var(--primary)" stroke-width="2.5"/>
          <text x="359" y="152" text-anchor="middle" fill="var(--muted-foreground)" font-size="10">Κυματοειδές αυλάκι βινυλίου</text>

          <text x="479" y="95" text-anchor="middle" fill="var(--primary)" font-size="14" font-weight="bold">⇄</text>

          <rect x="491" y="15" width="217" height="148" fill="var(--card)" stroke="currentColor" stroke-width="1.5"/>
          <text x="599" y="34" text-anchor="middle" fill="currentColor" font-size="11" font-weight="bold">3. ΗΧΗΤΙΚΑ ΚΥΜΑΤΑ (Schallwellen)</text>
          <line x1="504" y1="95" x2="696" y2="95" stroke="var(--border)" stroke-width="1"/>
          ${waveBars}
        </svg>
      `;

      readout.innerHTML = `<strong>Κοινή λογική δομή (<em>der logische Bau</em>, 4.014):</strong> <span class="math-expr">[${gramNotes.join(' — ')}]</span> &nbsp;|&nbsp; Παρότι οι 3 μορφές χρησιμοποιούν διαφορετικά υλικά (μελάνι σε πεντάγραμμο, αυλάκια σε δίσκο, πιέσεις αέρα), διαθέτουν την <strong>ίδια μαθηματική πολλαπλότητα (4.04)</strong> και μετασχηματίζονται η μία στην άλλη μέσω ενός νόμου προβολής (4.0141).`;
    }

    // -------------------------------------------------------------------------
    // 5. SCIENCE LAB: MESH (6.341), KANT 4D GLOVE, 2x2=4 (6.241), LADDER (6.54)
    // -------------------------------------------------------------------------
    let currentMeshType = 'square';
    let currentSpotPattern = 'blobs';
    let paintedSpots = [];
    let isPaintingSpots = false;

    function setMeshGeometry(type) {
      currentMeshType = type;
      ['square', 'triangle', 'hex'].forEach(t => {
        const b = document.getElementById('mesh-btn-' + t);
        if (b) b.classList.toggle('hw-btn-active', t === type);
      });
      drawMeshSimulation();
    }

    function setMeshSpotPattern(pat) {
      currentSpotPattern = pat;
      ['blobs', 'ring', 'paint'].forEach(p => {
        const b = document.getElementById('mesh-spot-' + p);
        if (b) b.classList.toggle('hw-btn-active', p === pat);
      });
      const clearBtn = document.getElementById('meshClearPaintBtn');
      if (clearBtn) clearBtn.hidden = (pat !== 'paint');
      drawMeshSimulation();
    }

    function clearPaintedSpots() { paintedSpots = []; drawMeshSimulation(); }

    function isInsideSpots(x, y) {
      if (currentSpotPattern === 'ring') {
        const dRing = Math.hypot(x - 210, y - 150);
        const dIsland = Math.hypot(x - 420, y - 145);
        return (dRing > 44 && dRing < 86) || (dIsland < 48);
      }
      if (currentSpotPattern === 'paint') {
        for (let i = 0; i < paintedSpots.length; i++) {
          const s = paintedSpots[i];
          if (Math.hypot(x - s.x, y - s.y) < s.r) return true;
        }
        return false;
      }
      const d1 = Math.hypot(x - 140, y - 130) + 12 * Math.sin(x * 0.08) + 10 * Math.cos(y * 0.08);
      const d2 = Math.hypot(x - 310, y - 165) + 15 * Math.cos(x * 0.06);
      const d3 = Math.hypot(x - 445, y - 110) + 10 * Math.sin(y * 0.09);
      return (d1 < 58) || (d2 < 64) || (d3 < 46);
    }

    function initMeshCanvasPainting() {
      const canvas = document.getElementById('meshCanvas');
      if (!canvas || canvas.dataset.paintBound) return;
      canvas.dataset.paintBound = '1';

      const addPt = (e) => {
        if (currentSpotPattern !== 'paint') return;
        const rect = canvas.getBoundingClientRect();
        const x = (e.clientX - rect.left) * (canvas.width / rect.width);
        const y = (e.clientY - rect.top) * (canvas.height / rect.height);
        paintedSpots.push({ x, y, r: 22 });
        drawMeshSimulation();
      };

      canvas.addEventListener('pointerdown', (e) => {
        if (currentSpotPattern !== 'paint') return;
        isPaintingSpots = true;
        addPt(e);
      });
      canvas.addEventListener('pointermove', (e) => {
        if (isPaintingSpots && currentSpotPattern === 'paint') addPt(e);
      });
      window.addEventListener('pointerup', () => { isPaintingSpots = false; });
    }

    function drawMeshSimulation() {
      const canvas = document.getElementById('meshCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const step = parseInt(document.getElementById('meshSizeSlider')?.value, 10) || 28;
      const lbl = document.getElementById('meshSizeLabel');
      if (lbl) lbl.textContent = step + 'px';

      const w = canvas.width;
      const h = canvas.height;
      const tokens = getComputedStyle(document.documentElement);
      const token = (name) => tokens.getPropertyValue(name).trim();
      const bgColor = token('--card') || '#fbfbf9';
      const spotColor = token('--foreground') || '#1c2022';
      const gridColor = token('--primary') || '#1e5c4e';
      const hitFill = token('--primary-hit') || 'rgba(30,92,78,0.28)';

      ctx.fillStyle = bgColor;
      ctx.fillRect(0, 0, w, h);

      ctx.fillStyle = spotColor;
      for (let py = 0; py < h; py += 3) {
        for (let px = 0; px < w; px += 3) {
          if (isInsideSpots(px, py)) ctx.fillRect(px, py, 3, 3);
        }
      }

      let totalCells = 0, blackCells = 0;
      ctx.strokeStyle = gridColor;
      ctx.lineWidth = 1;

      if (currentMeshType === 'square') {
        for (let y = 0; y < h; y += step) {
          for (let x = 0; x < w; x += step) {
            totalCells++;
            if (isInsideSpots(x + step / 2, y + step / 2)) {
              blackCells++;
              ctx.fillStyle = hitFill;
              ctx.fillRect(x, y, step, step);
            }
            ctx.strokeRect(x, y, step, step);
          }
        }
      } else if (currentMeshType === 'triangle') {
        for (let y = 0; y < h; y += step) {
          for (let x = 0; x < w; x += step) {
            totalCells++;
            ctx.beginPath();
            ctx.moveTo(x, y); ctx.lineTo(x + step, y); ctx.lineTo(x, y + step);
            ctx.closePath();
            if (isInsideSpots(x + step * 0.33, y + step * 0.33)) {
              blackCells++; ctx.fillStyle = hitFill; ctx.fill();
            }
            ctx.stroke();

            totalCells++;
            ctx.beginPath();
            ctx.moveTo(x + step, y); ctx.lineTo(x + step, y + step); ctx.lineTo(x, y + step);
            ctx.closePath();
            if (isInsideSpots(x + step * 0.67, y + step * 0.67)) {
              blackCells++; ctx.fillStyle = hitFill; ctx.fill();
            }
            ctx.stroke();
          }
        }
      } else {
        const r = step * 0.65;
        const dx = r * 1.5;
        const dy = r * Math.sqrt(3);
        for (let row = 0; row * dy < h + dy; row++) {
          for (let col = 0; col * dx < w + dx; col++) {
            totalCells++;
            const cx = col * dx;
            const cy = row * dy + (col % 2 === 1 ? dy / 2 : 0);
            ctx.beginPath();
            for (let k = 0; k < 6; k++) {
              const ang = (Math.PI / 3) * k;
              const vx = cx + r * Math.cos(ang);
              const vy = cy + r * Math.sin(ang);
              if (k === 0) ctx.moveTo(vx, vy); else ctx.lineTo(vx, vy);
            }
            ctx.closePath();
            if (isInsideSpots(cx, cy)) {
              blackCells++; ctx.fillStyle = hitFill; ctx.fill();
            }
            ctx.stroke();
          }
        }
      }

      const meshNameMap = {
        square: 'Τετραγωνικό δίχτυ (Νευτώνεια μηχανική)',
        triangle: 'Τριγωνικό δίχτυ (Εναλλακτικό αξιωματικό σύστημα)',
        hex: 'Εξαγωνικό δίχτυ'
      };
      const statsBox = document.getElementById('meshStatsBox');
      if (statsBox) {
        const pct = totalCells > 0 ? ((blackCells / totalCells) * 100).toFixed(1) : '0.0';
        statsBox.innerHTML = `
          <div><strong>Επιλεγμένο δίχτυ (6.341):</strong> ${meshNameMap[currentMeshType]}</div>
          <div><strong>Σύνολο οπών πλέγματος:</strong> ${totalCells} οπές (μέγεθος: ${step}px)</div>
          <div><strong>Καλυμμένες / λευκές οπές:</strong> ${blackCells} μαύρες (${pct}%) / ${totalCells - blackCells} λευκές</div>
        `;
      }
    }

    let kantAnimTimer = null;
    function renderKantHandSimulation() {
      const slider = document.getElementById('kantAngleSlider');
      const label = document.getElementById('kantAngleLabel');
      const svgBox = document.getElementById('kantSvgContainer');
      const status = document.getElementById('kantStatusText');
      if (!slider || !svgBox || !status) return;

      const deg = parseInt(slider.value, 10) || 0;
      label.textContent = deg + '°';
      const rad = (deg * Math.PI) / 180;
      const scaleX = Math.cos(rad);
      const shiftX = (deg / 180) * 190;
      const glovePath = 'M -22,42 L -22,8 C -22,-8 -20,-42 -13,-42 C -6,-42 -7,-12 -7,-12 L -5,-50 C -5,-56 4,-56 4,-50 L 5,-14 L 8,-46 C 8,-52 17,-52 17,-46 L 17,-10 L 21,-32 C 21,-38 29,-36 29,-30 L 26,6 C 32,2 40,-6 44,-2 C 48,3 41,16 32,25 L 24,42 Z';

      svgBox.innerHTML = `
        <svg viewBox="0 0 460 195" class="lab-svg" style="max-width:460px">
          <g transform="translate(320, 102) scale(-1, 1)">
            <path d="${glovePath}" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="5,4"/>
            <circle cx="8" cy="14" r="3.5" fill="currentColor"/>
          </g>
          <text x="320" y="175" text-anchor="middle" fill="currentColor" font-size="11.5" font-weight="bold">Αριστερό γάντι (b)</text>

          <g transform="translate(${130 + shiftX}, 102) scale(${scaleX.toFixed(3)}, 1)">
            <path d="${glovePath}" fill="var(--primary)" fill-opacity="0.24" stroke="var(--primary)" stroke-width="2.2"/>
            <circle cx="8" cy="14" r="3.5" fill="var(--primary)"/>
          </g>
          <text x="${130 + shiftX}" y="26" text-anchor="middle" fill="var(--primary)" font-size="11.5" font-weight="bold">Δεξί γάντι (a) [θ = ${deg}°]</text>
        </svg>
      `;

      if (deg === 0) {
        status.innerHTML = '<strong>θ = 0° (Ίδιος χώρος):</strong> Τα δύο γάντια a (δεξί) και b (αριστερό) είναι απολύτως ίσα (congruent), αλλά όσο μένουν εγκλωβισμένα στον ίδιο χώρο δεν μπορούν να συμπέσουν.';
      } else if (deg < 180) {
        status.innerHTML = `<strong>θ = ${deg}° (Περιστροφή μέσω της 4ης διάστασης):</strong> Το γάντι a εξέρχεται στον τετραδιάστατο χώρο (προβολικός συντελεστής cos θ = ${scaleX.toFixed(2)})...`;
      } else {
        status.innerHTML = '<strong>✓ θ = 180° (Πλήρης ταύτιση — 6.36111):</strong> Το δεξί γάντι περιστράφηκε μέσω του 4D χώρου και εφαρμόζει ακριβώς πάνω στο αριστερό.';
      }
    }

    function animateKantFlip() {
      const slider = document.getElementById('kantAngleSlider');
      if (!slider) return;
      if (kantAnimTimer) clearInterval(kantAnimTimer);
      let deg = 0;
      slider.value = 0;
      renderKantHandSimulation();
      kantAnimTimer = setInterval(() => {
        deg += 10;
        slider.value = deg;
        renderKantHandSimulation();
        if (deg >= 180) { clearInterval(kantAnimTimer); kantAnimTimer = null; }
      }, 45);
    }

    let currentMathStep = 0;
    const MATH_PROOF_STEPS = [
      {
        title: 'Βήμα 1: Ορισμός του γινομένου εκθετών (6.241)',
        eq: 'Ω^(2 × 2)\'x  =  (Ω²)²\'x',
        desc: 'Σύμφωνα με τον ορισμό του 6.241: (Ω^ν)^μ\'x = Ω^(ν×μ)\'x Def. Ο αριθμός 2 δεν είναι αντικείμενο, αλλά ο εκθέτης που δηλώνει διπλή εφαρμογή της πράξης Ω. Άρα το Ω^(2×2)\'x σημαίνει ότι εφαρμόζουμε τη σύνθετη πράξη (Ω²) δύο φορές.'
      },
      {
        title: 'Βήμα 2: Ανάπτυξη του εξωτερικού εκθέτη 2 = 1 + 1 (6.02)',
        eq: '(Ω²)²\'x  =  (Ω²)^(1 + 1)\'x  =  Ω²\'Ω²\'x',
        desc: 'Επειδή εξ ορισμού (6.02) ισχύει 2 = 0 + 1 + 1 = 1 + 1 και Ω^(ν+1)\'x = Ω\'Ω^ν\'x, η εξωτερική δύναμη 2 αναπτύσσεται σε δύο διαδοχικές εφαρμογές της πράξης Ω².'
      },
      {
        title: 'Βήμα 3: Αντικατάσταση του κάθε εσωτερικού Ω² (6.24)',
        eq: 'Ω²\'Ω²\'x  =  Ω^(1+1)\'Ω^(1+1)\'x  =  (Ω\'Ω)\'(Ω\'Ω)\'x',
        desc: 'Με τη μέθοδο της αντικατάστασης (Substitutionsmethode, 6.24), αντικαθιστούμε το κάθε Ω² με τη διπλή εφαρμογή (Ω\'Ω).'
      },
      {
        title: 'Βήμα 4: Καταμέτρηση των εφαρμογών της πράξης Ω ⟹ 2 × 2 = 4',
        eq: '(Ω\'Ω)\'(Ω\'Ω)\'x  =  Ω\'Ω\'Ω\'Ω\'x  =  Ω^(1+1+1+1)\'x  =  Ω⁴\'x',
        desc: 'Αφαιρούμε τις παρενθέσεις και βλέπουμε τέσσερις διαδοχικές εφαρμογές της πράξης Ω, οι οποίες εξ ορισμού (6.02) γράφονται ως Ω⁴\'x. Επομένως: 2 × 2 = 4.'
      }
    ];

    function setMathProofStep(idx) {
      currentMathStep = Math.max(0, Math.min(3, idx));
      for (let i = 0; i < 4; i++) {
        const b = document.getElementById('math-step-' + i);
        if (b) b.classList.toggle('hw-btn-active', i === currentMathStep);
      }
      const prevBtn = document.getElementById('mathPrevBtn');
      const nextBtn = document.getElementById('mathNextBtn');
      if (prevBtn) prevBtn.disabled = currentMathStep === 0;
      if (nextBtn) nextBtn.disabled = currentMathStep === 3;

      const box = document.getElementById('mathProofDisplay');
      if (!box) return;
      const st = MATH_PROOF_STEPS[currentMathStep];
      box.innerHTML = `
        <div class="lab-kicker accent-text">${st.title}</div>
        <div class="math-proof-eq">${st.eq}</div>
        <div class="math-proof-desc">${st.desc}</div>
      `;
    }

    function stepMathProof(delta) { setMathProofStep(currentMathStep + delta); }

    let currentLadderRung = 1;
    let isLadderThrown = false;
    let ladderReadingMode = 'traditional';
    const LADDER_RUNGS = [
      { n: 1, title: '1. Ο κόσμος', sub: 'Tatsachen (1–1.21)' },
      { n: 2, title: '2. Η εικόνα', sub: 'Bildtheorie (2–2.225)' },
      { n: 3, title: '3. Η σκέψη', sub: 'Satzzeichen (3–3.5)' },
      { n: 4, title: '4. Ο λόγος', sub: 'Λέγειν / Δεικνύναι (4.12)' },
      { n: 5, title: '5. Πράξεις N(ξ̄)', sub: 'Σολιψισμός (5.64)' },
      { n: 6, title: '6. [p̄, ξ̄, N(ξ̄)]', sub: 'Η σκάλα (6.54)' },
      { n: 7, title: '7. Η σιωπή', sub: 'Schweigen (7)' }
    ];

    function setLadderRung(n) { isLadderThrown = false; currentLadderRung = n; renderLadder(); }

    function setLadderReading(mode) {
      ladderReadingMode = mode;
      document.getElementById('ladder-read-trad').classList.toggle('hw-btn-active', mode === 'traditional');
      document.getElementById('ladder-read-ther').classList.toggle('hw-btn-active', mode === 'therapeutic');
      document.getElementById('ladder-read-eluc').classList.toggle('hw-btn-active', mode === 'elucidatory');
      renderLadder();
    }

    function renderLadder() {
      const area = document.getElementById('ladderInteractiveArea');
      const comm = document.getElementById('ladderCommentaryBox');
      if (!area || !comm) return;

      area.innerHTML = `
        <div class="ladder-grid">
          ${LADDER_RUNGS.map((r, idx) => {
            const active = (!isLadderThrown && r.n <= currentLadderRung) || (isLadderThrown && r.n === 7);
            const faded = (isLadderThrown && r.n < 7);
            return `
              <button type="button" onclick="setLadderRung(${r.n})"
                style="--rung-lift: ${idx * 14}px;"
                class="ladder-rung${active ? ' is-active' : ''}${faded ? ' is-thrown' : ''}">
                <span class="ladder-step">Σκαλί ${r.n}</span>
                <span class="ladder-title">${r.title}</span>
                <span class="ladder-sub">${r.sub}</span>
              </button>
            `;
          }).join('')}
        </div>
      `;

      if (isLadderThrown) {
        if (ladderReadingMode === 'traditional') {
          comm.innerHTML = '<strong>✓ Η σκάλα πετάχτηκε — Παραδοσιακή ανάγνωση (Anscombe, Hacker, Pears):</strong> Οι προτάσεις 1–6.53 είναι τυπικά <em>unsinnig</em> (παραβιάζουν τη λογική σύνταξη), αλλά λειτούργησαν ως «φωτιστική ανοησία» που μας επέτρεψε να δούμε ανείπωτες λογικές αλήθειες (<em>δείχνονται</em>) πριν περάσουμε στη σιωπή (7).';
        } else if (ladderReadingMode === 'elucidatory') {
          comm.innerHTML = '<strong>✓ Η σκάλα πετάχτηκε — Διασαφητική ανάγνωση (McGinn, Hutto):</strong> Ενδιάμεση θέση. Δέχεται την κριτική της Diamond στις «άρρητες αλήθειες», αλλά θεωρεί ότι το βιβλίο δίνει θετική επίγνωση της λογικής της γλώσσας. Οι Hutchinson και Read αντιτείνουν ότι η μέση αυτή θέση ξαναγλιστρά στο άρρητο.';
        } else {
          comm.innerHTML = '<strong>✓ Η σκάλα πετάχτηκε — Αποφασιστική ανάγνωση / New Wittgenstein (Diamond, Conant):</strong> Δεν υπάρχει «βαθιά άρρητη μεταφυσική» πίσω από τις προτάσεις. Το <em>Unsinn</em> είναι απλώς ασυναρτησία: ο αναγνώστης απαλλάσσεται από την ψευδαίσθηση ότι οι προτάσεις 1–6.53 διατύπωναν κάποια θεωρία, και αφήνει πίσω του ολόκληρη τη μεταφυσική σκαλωσιά.';
        }
      } else {
        comm.innerHTML = `<strong>Βρίσκεστε στο σκαλί ${currentLadderRung} από 7:</strong> Χρησιμοποιούμε τις προτάσεις του <em>Tractatus</em> ως σκαλοπάτια διασάφησης (<em>Erläuterungen</em>). Φτάστε στο σκαλί 7 και πατήστε <strong>«Πέταξε τη σκάλα (6.54)»</strong>.`;
      }
    }

    function climbLadderStep() { isLadderThrown = false; if (currentLadderRung < 7) currentLadderRung++; renderLadder(); }
    function throwAwayLadder() { currentLadderRung = 7; isLadderThrown = true; renderLadder(); }
    function resetLadder() { currentLadderRung = 1; isLadderThrown = false; renderLadder(); }

    // -------------------------------------------------------------------------
    // 6. 12 PHILOSOPHERS COMPARISON CARDS
    // -------------------------------------------------------------------------
    function renderPhilosophersGrid(cat, highlightId = null) {
      const container = document.getElementById('philosophersGridContainer');
      if (!container) return;
      const q = normSearch((document.getElementById('philSearchInput')?.value || '').trim());
      const list = PHILOSOPHERS_DATA.filter(p => {
        if (cat !== 'all' && p.cat !== cat) return false;
        if (q) {
          return normSearch(p.name + ' ' + p.ref + ' ' + p.oldView + ' ' + p.wittView).includes(q);
        }
        return true;
      });
      if (list.length === 0) {
        container.innerHTML = '<div class="lab-empty">Δεν βρέθηκαν στοχαστές με αυτά τα κριτήρια.</div>';
        return;
      }
      container.innerHTML = list.map(p => `
        <article id="phil-${escHtml(p.id)}" class="phil-card${highlightId === p.id ? ' is-highlighted' : ''}">
          <div class="phil-head">
            <h3>${escHtml(p.name)}</h3>
            <span class="hw-badge">${escHtml(p.ref)}</span>
          </div>
          <div class="phil-block">
            <div class="phil-sublabel">Παραδοσιακή θέση</div>
            <p>${escHtml(p.oldView)}</p>
          </div>
          <div class="phil-block phil-block-witt">
            <div class="phil-sublabel accent-text">Η ανατροπή / σύνθεση στο Tractatus</div>
            <p>${escHtml(p.wittView)}</p>
          </div>
        </article>
      `).join('');
    }
