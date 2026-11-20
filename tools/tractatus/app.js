    // =========================================================================
    // PAGE CONTROLLER: THEME, TABS, DEEP LINKS, SEARCH, SCROLLSPY, KATEX
    // =========================================================================

    function normSearch(str) {
      return String(str || '')
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .toLowerCase();
    }

    function buildNormMap(str) {
      let norm = '';
      const starts = [];
      for (let i = 0; i < str.length; i++) {
        const ch = str[i].normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        for (let k = 0; k < ch.length; k++) {
          norm += ch[k];
          starts.push(i);
        }
      }
      starts.push(str.length);
      return { norm, starts };
    }

    // -------------------------------------------------------------------------
    // 1. HEADER HEIGHT, THEME & SIDEBAR FOLD
    // -------------------------------------------------------------------------
    let currentArchTheme = 'light';

    function updateHeaderHeightVar() {
      const h = document.getElementById('siteHeader');
      if (h) {
        document.documentElement.style.setProperty('--header-h', h.offsetHeight + 'px');
      }
    }

    function applyArchPalette(mode, persist = true) {
      currentArchTheme = mode;
      const root = document.documentElement;
      root.classList.toggle('dark', mode === 'dark');
      root.classList.toggle('light', mode !== 'dark');
      const tBtn = document.getElementById('themeToggleBtn');
      if (tBtn) {
        tBtn.textContent = mode === 'dark' ? 'Φωτεινό θέμα' : 'Σκοτεινό θέμα';
      }
      if (persist) {
        try { localStorage.setItem('hw-tlp-theme', mode); } catch (e) {}
      }
      drawMeshSimulation();
    }

    function initThemeIfNeeded() {
      let saved = null;
      try { saved = localStorage.getItem('hw-tlp-theme'); } catch (e) {}
      applyArchPalette(saved === 'dark' ? 'dark' : 'light', false);
    }

    function toggleArchitecturalTheme() {
      applyArchPalette(currentArchTheme === 'light' ? 'dark' : 'light', true);
    }

    function applySidebarFold(folded, persist = true) {
      document.documentElement.classList.toggle('sidebar-folded', folded);
      const btn = document.getElementById('sidebarFoldBtn');
      if (btn) {
        const label = folded ? 'Ανάπτυξη περιεχομένων' : 'Σύμπτυξη περιεχομένων';
        btn.setAttribute('aria-expanded', folded ? 'false' : 'true');
        btn.setAttribute('aria-label', label);
        btn.title = label + ' (πλήκτρο [)';
      }
      if (persist) {
        try { localStorage.setItem('hw-tlp-sidebar', folded ? 'folded' : 'open'); } catch (e) {}
      }
    }

    function toggleSidebarFold() {
      applySidebarFold(!document.documentElement.classList.contains('sidebar-folded'), true);
    }

    function initSidebarFold() {
      let saved = null;
      try { saved = localStorage.getItem('hw-tlp-sidebar'); } catch (e) {}
      applySidebarFold(saved === 'folded', false);
    }

    // -------------------------------------------------------------------------
    // 2. TAB SWITCHING, DEEP-LINK ROUTING & MOBILE DRAWER
    // -------------------------------------------------------------------------
    const MAIN_TABS = ['master', 'tree', 'logic', 'visual', 'science', 'philosophers'];
    const LAB_TO_TAB = {
      'lab-truth-tables': 'logic',
      'lab-wpf': 'logic',
      'lab-probability': 'logic',
      'lab-paris': 'visual',
      'lab-necker': 'visual',
      'lab-eye': 'visual',
      'lab-gramophone': 'visual',
      'lab-mesh': 'science',
      'lab-kant': 'science',
      'lab-2x2': 'science',
      'lab-ladder': 'science'
    };
    let currentMainTab = 'master';

    function pulseHighlight(el) {
      if (!el) return;
      el.classList.remove('is-highlighted');
      void el.offsetWidth;
      el.classList.add('is-highlighted');
      setTimeout(() => { el.classList.remove('is-highlighted'); }, 2200);
    }

    function switchMainTab(tabId, skipScroll = false, updateHash = true) {
      if (!MAIN_TABS.includes(tabId)) tabId = 'master';
      currentMainTab = tabId;
      document.body.dataset.tab = tabId;

      MAIN_TABS.forEach(t => {
        const viewEl = document.getElementById('view-' + t);
        const btnEl = document.getElementById('tab-btn-' + t);
        const active = (t === tabId);
        if (viewEl) {
          viewEl.hidden = !active;
          if (active) {
            viewEl.classList.remove('view-animate');
            void viewEl.offsetWidth;
            viewEl.classList.add('view-animate');
          }
        }
        if (btnEl) {
          btnEl.classList.toggle('hw-btn-active', active);
          btnEl.setAttribute('aria-selected', active ? 'true' : 'false');
        }
      });

      if (tabId === 'tree') renderTreeExplorer();
      if (tabId === 'logic') {
        updateTruthTableDiagnosis();
        renderWpfDiagram(currentWpfMode);
        calculateLogicalProbability();
      }
      if (tabId === 'visual') {
        updateParisSimulation();
        setNeckerMode(currentNeckerMode);
        setEyeDiagramMode(currentEyeMode);
        renderGramophoneLab();
      }
      if (tabId === 'science') {
        drawMeshSimulation();
        renderKantHandSimulation();
        setMathProofStep(currentMathStep);
        renderLadder();
      }
      if (tabId === 'philosophers') {
        renderPhilosophersGrid(document.getElementById('philFilterSelect')?.value || 'all');
      }

      if (updateHash) {
        try { history.replaceState(null, '', '#tab=' + tabId); } catch (e) {}
      }
      if (!skipScroll) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
      updateReadingProgress();
    }

    function filterMasterSections(sectionId) {
      document.querySelectorAll('.master-section').forEach(sec => {
        sec.hidden = !(sectionId === 'all' || sec.id === sectionId);
      });
      const selDesktop = document.getElementById('sectionFilterSelect');
      if (selDesktop && selDesktop.value !== sectionId) selDesktop.value = sectionId;
      const selMobile = document.querySelector('#mobileNavMount select');
      if (selMobile && selMobile.value !== sectionId) selMobile.value = sectionId;
    }

    function ensureSectionVisible(sectionId) {
      const sel = document.getElementById('sectionFilterSelect');
      if (sel && sel.value !== 'all' && sel.value !== sectionId) {
        filterMasterSections('all');
      }
    }

    function navigateMasterAnchor(sectionId) {
      ensureSectionVisible(sectionId);
      closeMobileNav();
    }

    function jumpToAnalysisAnchor(anchor, instant = false) {
      const id = String(anchor || '').replace(/^#/, '');
      if (!id) return;
      if (currentMainTab !== 'master') {
        switchMainTab('master', true, false);
      }
      const target = document.getElementById(id);
      if (!target) return;
      const sec = target.closest('.master-section');
      if (sec) ensureSectionVisible(sec.id);
      try { history.replaceState(null, '', '#' + id); } catch (e) {}
      target.scrollIntoView({ behavior: instant ? 'instant' : 'smooth', block: 'start' });
      pulseHighlight(target);
    }

    function jumpToLab(labId, instant = false) {
      const id = String(labId || '').replace(/^#/, '');
      const tab = LAB_TO_TAB[id];
      if (!tab) return false;
      switchMainTab(tab, true, false);
      try { history.replaceState(null, '', '#' + id); } catch (e) {}
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) {
          el.scrollIntoView({ behavior: instant ? 'instant' : 'smooth', block: 'start' });
          pulseHighlight(el);
        }
      }, instant ? 0 : 40);
      return true;
    }

    function jumpToPhilosopher(philId, instant = false) {
      const slug = String(philId || '').replace(/^#?phil-/, '');
      if (!slug) return false;
      const inp = document.getElementById('philSearchInput');
      const sel = document.getElementById('philFilterSelect');
      if (inp) inp.value = '';
      if (sel) sel.value = 'all';
      switchMainTab('philosophers', true, false);
      renderPhilosophersGrid('all', slug);
      try { history.replaceState(null, '', '#phil-' + slug); } catch (e) {}
      setTimeout(() => {
        const el = document.getElementById('phil-' + slug);
        if (el) {
          el.scrollIntoView({ behavior: instant ? 'instant' : 'smooth', block: 'center' });
          pulseHighlight(el);
        }
      }, instant ? 0 : 40);
      return true;
    }

    function openMobileNav() {
      const drawer = document.getElementById('mobileNavDrawer');
      const mount = document.getElementById('mobileNavMount');
      const src = document.getElementById('sidebarInnerContent');
      if (mount && src && !mount.hasChildNodes()) {
        mount.innerHTML = src.innerHTML;
        const mSel = mount.querySelector('select');
        if (mSel) {
          mSel.removeAttribute('id');
          mSel.value = document.getElementById('sectionFilterSelect')?.value || 'all';
        }
        const mNav = mount.querySelector('nav');
        if (mNav) mNav.removeAttribute('id');
      }
      if (drawer) drawer.hidden = false;
    }

    function closeMobileNav() {
      const drawer = document.getElementById('mobileNavDrawer');
      if (drawer) drawer.hidden = true;
    }

    // Intercept internal cross-tab links (#lab-*, #phil-*, #concept-*, #prop-*, #branch-*, #term-*)
    document.addEventListener('click', (e) => {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const href = a.getAttribute('href') || '';
      const id = href.slice(1);
      if (LAB_TO_TAB[id]) {
        e.preventDefault();
        jumpToLab(id);
      } else if (id.startsWith('phil-')) {
        e.preventDefault();
        openPhilPeek(id.slice(5));
      } else if (id.startsWith('concept-')) {
        e.preventDefault();
        openConceptPeek(id.slice(8));
      } else if (id === 'tab=tree') {
        e.preventDefault();
        switchMainTab('tree');
      } else if (id.startsWith('prop-') || id.startsWith('branch-') || id.startsWith('term-')) {
        e.preventDefault();
        jumpToAnalysisAnchor(id);
      }
    });

    // -------------------------------------------------------------------------
    // 3. ACCENT-INSENSITIVE GLOBAL SEARCH (SAFE FOR KATEX)
    // -------------------------------------------------------------------------
    let searchHitElements = [];
    let currentSearchHitIdx = -1;

    function clearDomHighlights() {
      document.querySelectorAll('#masterContentContainer mark.search-hit').forEach(mark => {
        const parent = mark.parentNode;
        if (!parent) return;
        parent.replaceChild(document.createTextNode(mark.textContent), mark);
        parent.normalize();
      });
      searchHitElements = [];
      currentSearchHitIdx = -1;
    }

    function highlightTextInElement(rootEl, qNorm) {
      const walker = document.createTreeWalker(rootEl, NodeFilter.SHOW_TEXT, {
        acceptNode(node) {
          if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
          const p = node.parentNode;
          if (!p) return NodeFilter.FILTER_REJECT;
          const tag = p.nodeName;
          if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'MARK' || tag === 'TEXTAREA' || tag === 'INPUT' || tag === 'BUTTON' || tag === 'SELECT' || tag === 'OPTION') {
            return NodeFilter.FILTER_REJECT;
          }
          if (p.closest && (p.closest('.katex') || p.closest('.katex-mathml') || p.closest('svg'))) {
            return NodeFilter.FILTER_REJECT;
          }
          return normSearch(node.nodeValue).includes(qNorm) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
        }
      });

      const nodesToWrap = [];
      while (walker.nextNode()) nodesToWrap.push(walker.currentNode);

      nodesToWrap.forEach(textNode => {
        const val = textNode.nodeValue;
        const { norm, starts } = buildNormMap(val);
        const frag = document.createDocumentFragment();
        let lastOrig = 0;
        let idx = norm.indexOf(qNorm, 0);
        while (idx !== -1) {
          const origStart = starts[idx];
          const origEnd = starts[idx + qNorm.length];
          if (origStart > lastOrig) {
            frag.appendChild(document.createTextNode(val.slice(lastOrig, origStart)));
          }
          const mark = document.createElement('mark');
          mark.className = 'search-hit';
          mark.textContent = val.slice(origStart, origEnd);
          frag.appendChild(mark);
          searchHitElements.push(mark);
          lastOrig = origEnd;
          idx = norm.indexOf(qNorm, idx + qNorm.length);
        }
        if (lastOrig < val.length) {
          frag.appendChild(document.createTextNode(val.slice(lastOrig)));
        }
        textNode.parentNode.replaceChild(frag, textNode);
      });
    }

    function stepSearchHit(delta) {
      if (searchHitElements.length === 0) return;
      if (currentMainTab !== 'master') {
        switchMainTab('master', true, false);
      }
      if (currentSearchHitIdx >= 0 && searchHitElements[currentSearchHitIdx]) {
        searchHitElements[currentSearchHitIdx].classList.remove('search-hit-active');
      }
      currentSearchHitIdx = (currentSearchHitIdx + delta + searchHitElements.length) % searchHitElements.length;
      const el = searchHitElements[currentSearchHitIdx];
      // If hit is inside a collapsed <details class="prop-orig">, open it
      const det = el.closest && el.closest('details');
      if (det) det.open = true;
      el.classList.add('search-hit-active');
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      const posEl = document.getElementById('searchHitPos');
      if (posEl) posEl.textContent = (currentSearchHitIdx + 1) + ' / ' + searchHitElements.length;
    }

    function handleGlobalSearch(query) {
      const clearBtn = document.getElementById('clearSearchBtn');
      const navBar = document.getElementById('searchNavBar');
      const badge = document.getElementById('searchCountBadge');
      const hitControls = document.getElementById('searchHitControls');
      const hitPos = document.getElementById('searchHitPos');
      const crossLinks = document.getElementById('searchCrossViewLinks');
      const rawQ = (query || '').trim();
      const qNorm = normSearch(rawQ);

      clearDomHighlights();

      if (!qNorm) {
        if (clearBtn) clearBtn.hidden = true;
        if (navBar) navBar.hidden = true;
        filterMasterSections(document.getElementById('sectionFilterSelect')?.value || 'all');
        updateHeaderHeightVar();
        return;
      }

      if (clearBtn) clearBtn.hidden = false;
      if (navBar) navBar.hidden = false;
      updateHeaderHeightVar();

      document.querySelectorAll('.master-section').forEach(sec => {
        // Use textContent so collapsed <details> originals are also searched
        const hay = normSearch(sec.textContent || '');
        if (hay.includes(qNorm)) {
          sec.hidden = false;
          highlightTextInElement(sec, qNorm);
        } else {
          sec.hidden = true;
        }
      });

      const masterHits = searchHitElements.length;
      if (badge) badge.textContent = masterHits + ' ευρήματα στην Ανάλυση';

      if (masterHits > 0) {
        if (hitControls) hitControls.hidden = false;
        currentSearchHitIdx = 0;
        const first = searchHitElements[0];
        const det = first.closest && first.closest('details');
        if (det) det.open = true;
        first.classList.add('search-hit-active');
        if (hitPos) hitPos.textContent = '1 / ' + masterHits;
      } else {
        if (hitControls) hitControls.hidden = true;
      }

      const treeMatches = TLP_TREE_DATA.filter(item =>
        normSearch([item.num, item.title || '', item.de || '', item.ogden || '', item.pm || '', item.el || '', item.note || ''].join(' ').replace(/\$/g, '')).includes(qNorm)
      ).length;
      const philMatches = PHILOSOPHERS_DATA.filter(p =>
        normSearch(p.name + ' ' + p.ref + ' ' + p.oldView + ' ' + p.wittView).includes(qNorm)
      ).length;

      const pills = [];
      const safeQ = rawQ.replace(/\\/g, '\\\\').replace(/'/g, "\\'");
      if (currentMainTab !== 'master' && masterHits > 0) {
        pills.push(`<button type="button" onclick="switchMainTab('master', true)" class="hw-btn">Ανάλυση (${masterHits})</button>`);
      }
      if (treeMatches > 0) {
        pills.push(`<button type="button" onclick="jumpSearchToTree('${safeQ}')" class="hw-btn">Δενδροειδής μορφή: ${treeMatches}</button>`);
      }
      if (philMatches > 0) {
        pills.push(`<button type="button" onclick="jumpSearchToPhil('${safeQ}')" class="hw-btn">Φιλόσοφοι: ${philMatches}</button>`);
      }
      if (crossLinks) crossLinks.innerHTML = pills.join('');
    }

    function jumpSearchToTree(q) {
      const inp = document.getElementById('treeSearchInput');
      const rSel = document.getElementById('treeRootFilter');
      const lSel = document.getElementById('treeLevelFilter');
      if (inp) inp.value = q;
      if (rSel) rSel.value = 'all';
      if (lSel) lSel.value = 'all';
      switchMainTab('tree');
    }

    function jumpSearchToPhil(q) {
      const inp = document.getElementById('philSearchInput');
      const sel = document.getElementById('philFilterSelect');
      if (inp) inp.value = q;
      if (sel) sel.value = 'all';
      switchMainTab('philosophers');
    }

    function clearGlobalSearch() {
      const input = document.getElementById('globalSearchInput');
      if (input) input.value = '';
      handleGlobalSearch('');
    }

    // -------------------------------------------------------------------------
    // 4. KATEX RENDERING, SCROLLSPY, PROGRESS & KEYBOARD SHORTCUTS
    // -------------------------------------------------------------------------
    function renderOneMathEl(el) {
      if (!window.katex || !el || el.classList.contains('tex-done')) return;
      const tex = el.dataset.texSrc != null ? el.dataset.texSrc : el.textContent;
      el.dataset.texSrc = tex;
      el.classList.add('tex-done');
      el.classList.remove('tex-queued');
      try {
        window.katex.render(tex, el, { displayMode: el.classList.contains('tex-display'), throwOnError: false });
      } catch (e) { el.textContent = tex; }
    }

    function renderMathIn(root) {
      if (!window.katex || !root) return;
      const els = root.querySelectorAll('.tex:not(.tex-done)');
      for (let i = 0; i < els.length; i++) {
        renderOneMathEl(els[i]);
      }
    }

    function renderAllMath() {
      if (!window.katex) return;
      const els = Array.prototype.slice.call(document.querySelectorAll('.tex:not(.tex-done):not(.tex-queued)'));
      if (els.length === 0) return;
      for (let k = 0; k < els.length; k++) {
        els[k].classList.add('tex-queued');
      }
      let i = 0;
      function batch() {
        const end = Math.min(i + 24, els.length);
        for (; i < end; i++) {
          renderOneMathEl(els[i]);
        }
        if (i < els.length) setTimeout(batch, 16);
      }
      batch();
    }

    function updateReadingProgress() {
      const bar = document.getElementById('readingProgressBar');
      const topBtn = document.getElementById('backToTopBtn');
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? Math.min(100, Math.max(0, (window.scrollY / docHeight) * 100)) : 0;
      if (bar) bar.style.width = pct.toFixed(1) + '%';
      if (topBtn) topBtn.hidden = (window.scrollY < 420);
    }

    function initScrollSpy() {
      if (!('IntersectionObserver' in window)) return;
      const links = Array.from(document.querySelectorAll('#masterNavList .idx-row'));
      const targetIds = links.map(l => (l.getAttribute('href') || '').slice(1)).filter(Boolean);
      const targets = targetIds.map(id => document.getElementById(id)).filter(Boolean);
      if (targets.length === 0) return;

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            links.forEach(l => {
              const match = (l.getAttribute('href') === '#' + id);
              l.classList.toggle('hw-nav-active', match);
            });
          }
        });
      }, { rootMargin: '-18% 0px -72% 0px', threshold: 0 });

      targets.forEach(el => observer.observe(el));
    }

    function applyInitialHash() {
      const hash = window.location.hash || '';
      if (!hash) return;
      if (hash.startsWith('#tab=')) {
        const tab = hash.slice(5);
        if (MAIN_TABS.includes(tab)) switchMainTab(tab, true, false);
        return;
      }
      const id = hash.slice(1);
      if (LAB_TO_TAB[id]) {
        jumpToLab(id, true);
      } else if (id.startsWith('phil-')) {
        jumpToPhilosopher(id, true);
      } else if (id.startsWith('concept-')) {
        openConceptPeek(id.slice(8));
      } else if (document.getElementById(id)) {
        jumpToAnalysisAnchor(id, true);
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      initThemeIfNeeded();
      initSidebarFold();
      updateHeaderHeightVar();
      if ('ResizeObserver' in window) {
        const ro = new ResizeObserver(updateHeaderHeightVar);
        const h = document.getElementById('siteHeader');
        if (h) ro.observe(h);
      }

      bindInteractiveRefs();
      renderTreeExplorer();
      updateTruthTableDiagnosis();
      renderWpfDiagram('noncontra');
      calculateLogicalProbability();
      updateParisSimulation();
      setNeckerMode('a-front');
      setEyeDiagramMode('limit');
      renderGramophoneLab();
      initMeshCanvasPainting();
      drawMeshSimulation();
      renderKantHandSimulation();
      setMathProofStep(0);
      renderLadder();
      renderPhilosophersGrid('all');
      initScrollSpy();
      applyInitialHash();
      updateReadingProgress();
      renderAllMath();
    });

    window.addEventListener('load', renderAllMath);
    window.addEventListener('scroll', updateReadingProgress, { passive: true });
    window.addEventListener('resize', () => {
      updateHeaderHeightVar();
      if (currentMainTab === 'tree') renderTreeExplorer();
    });
    window.addEventListener('hashchange', applyInitialHash);

    window.addEventListener('keydown', (e) => {
      const tag = document.activeElement?.tagName;
      const inInput = tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT';

      if (e.key === 'Escape') {
        closePeek();
        closeMobileNav();
        if (document.activeElement === document.getElementById('globalSearchInput')) {
          clearGlobalSearch();
          document.activeElement.blur();
        }
        return;
      }

      if (document.activeElement === document.getElementById('globalSearchInput') && e.key === 'Enter') {
        e.preventDefault();
        stepSearchHit(e.shiftKey ? -1 : 1);
        return;
      }

      if (inInput) return;

      if (e.key === '/') {
        e.preventDefault();
        const inp = document.getElementById('globalSearchInput');
        if (inp) { inp.focus(); inp.select(); }
      } else if (e.key === '[') {
        if (currentMainTab === 'master') toggleSidebarFold();
      } else if (e.key >= '1' && e.key <= '6') {
        const idx = parseInt(e.key, 10) - 1;
        if (MAIN_TABS[idx]) switchMainTab(MAIN_TABS[idx]);
      }
    });
