/* 스피드 배관공사 — 경량 인터랙션 (vanilla JS)
   콘텐츠는 모두 HTML에 렌더링되어 있으며, JS는 보조 동작만 담당합니다. */
(function () {
  "use strict";

  /* ---------- 1. 스크롤 시 헤더 흰색 전환 ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 24) header.classList.add("is-scrolled");
      else header.classList.remove("is-scrolled");
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- 2. 모바일 메뉴 토글 ---------- */
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------- 3. 모바일 서브메뉴 펼침 ---------- */
  document.querySelectorAll(".gnb .has-sub > .gnb-link").forEach(function (link) {
    link.addEventListener("click", function (e) {
      // 데스크탑(hover)에서는 막지 않음 — 모바일 폭에서만 토글
      if (window.matchMedia("(max-width:1024px)").matches) {
        e.preventDefault();
        link.parentElement.classList.toggle("is-expanded");
      }
    });
  });

  /* ---------- 4. FAQ 아코디언 ---------- */
  document.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var open = item.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  /* ---------- 5. 메뉴 링크 클릭 시 모바일 메뉴 닫기 ---------- */
  document.querySelectorAll(".gnb a:not(.has-sub > .gnb-link)").forEach(function (a) {
    a.addEventListener("click", function () {
      document.body.classList.remove("nav-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---------- 6. 견적 폼 (데모: 실제 전송 없이 안내) ---------- */
  var form = document.querySelector("form[data-quote-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = form.querySelector(".form-status");
      if (msg) {
        msg.hidden = false;
        msg.textContent = "상담 신청이 접수되었습니다. 빠르게 연락드리겠습니다. (데모 폼)";
      }
      form.reset();
    });
  }
})();
