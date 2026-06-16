#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""모든 페이지 콘텐츠 정의 후 빌드. 사용: python3 pages.py"""
from build import (page, SITE, breadcrumb_jsonld, SIDEBAR, bottom_cta)

S = SITE

# ===========================================================================
# 홈 (index.html)
# ===========================================================================
HOME_JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "name": "스피드 배관공사",
  "alternateName": "SPEED PLUMBING",
  "description": "호텔·상가·오피스빌딩 등 상업시설 전문 B2B 배관 파트너. 하수구막힘·배관공사·누수탐지·고압세척 24시간 출동.",
  "image": "%(s)s/assets/logo/symbol.png",
  "logo": "%(s)s/assets/logo/logo-horizontal-dark.png",
  "url": "%(s)s/",
  "telephone": "+82-1577-0000",
  "priceRange": "\\u20a9\\u20a9",
  "openingHoursSpecification": {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"},
  "areaServed": {"@type":"Country","name":"대한민국"},
  "address": {"@type":"PostalAddress","addressCountry":"KR","addressRegion":"서울특별시"},
  "aggregateRating": {"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"327"}
}
</script>
""" % {"s": S}

FAQ_ITEMS = [
    ("상업시설 출동은 정말 24시간 가능한가요?",
     "네. 호텔·상가·오피스빌딩 등 상업시설은 영업 중단이 곧 손실이므로 야간·휴일을 포함한 24시간 긴급 출동 체계를 운영합니다. 접수 즉시 가까운 작업팀이 배정됩니다."),
    ("작업 전에 견적을 먼저 받을 수 있나요?",
     "선견적 후작업이 원칙입니다. 현장 진단 후 비용과 작업 범위를 명확히 안내하고, 동의하신 뒤에 작업을 시작합니다. 사전 협의 없는 추가금은 청구하지 않습니다."),
    ("하수구막힘이 반복되는데 원인을 찾을 수 있나요?",
     "CCTV 관로 검사로 배관 내부를 확인해 막힘·파손·기름때 누적 등 근본 원인을 진단합니다. 일시적 뚫음이 아니라 고압세척·부분 교체 등 재발 방지 방안을 함께 제안합니다."),
    ("누수 위치를 벽을 뜯지 않고 찾을 수 있나요?",
     "청음식 누수탐지기·열화상 카메라·가스 탐지 등 비파괴 장비로 누수 지점을 특정합니다. 불필요한 철거를 최소화해 복구 비용과 시간을 줄입니다."),
    ("전국 어디든 출동이 되나요?",
     "전국 시·도 네트워크를 통해 주요 도시 및 인근 시·군·구로 출동합니다. 지역별 서비스 페이지에서 가능 지역을 확인하거나 전화로 문의해 주세요."),
    ("세금계산서·현금영수증 발행이 가능한가요?",
     "가능합니다. 상업시설 B2B 거래 특성상 세금계산서, 거래명세서, 현금영수증 발행을 지원하며 정기 관리 계약도 협의할 수 있습니다."),
]

def faq_jsonld(items):
    q = []
    for name, ans in items:
        q.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                  % (name.replace('"', '\\"'), ans.replace('"', '\\"')))
    return ('<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
            + ",".join(q) + "]}\n</script>\n")

def faq_html(items, intro=True):
    rows = ""
    for name, ans in items:
        rows += f"""      <div class="faq-item">
        <button class="faq-q" aria-expanded="false"><span>{name}</span><span class="plus" aria-hidden="true"></span></button>
        <div class="faq-a"><div class="faq-a-inner">{ans}</div></div>
      </div>
"""
    return rows

HERO = """<section class="hero">
  <div class="container hero-inner">
    <span class="badge badge--light"><span class="dot"></span>호텔 · 상가 · 오피스빌딩 전문 B2B 배관</span>
    <h1>호텔·상가·빌딩 배관,<br><span class="accent">멈추지 않는 신속함.</span></h1>
    <p class="hero-sub">하수구막힘·배관공사·누수탐지·고압세척 — 영업 손실을 만들지 않는 24시간 상업시설 전문 출동. 선견적 후작업으로 추가금 걱정 없이 신뢰할 수 있습니다.</p>
    <div class="hero-cta">
      <a class="btn btn--primary btn--lg" href="tel:1577-0000">
        <svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.68 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.32 1.85.55 2.81.68A2 2 0 0 1 22 16.92z"/></svg>
        지금 전화 1577-0000</a>
      <a class="btn btn--ghost-light btn--lg" href="/contact.html">무료 견적 받기</a>
    </div>
    <div class="hero-trust">
      <span class="badge badge--light">⏱ 평균 30분 내 출동</span>
      <span class="badge badge--light">✓ 선견적 후작업 · 추가금 없음</span>
      <span class="badge badge--light">★ 누적 4.9 / 327건 후기</span>
    </div>
    <div class="hero-keywords" aria-hidden="true">
      <span>#배관공사</span><span>#하수구막힘</span><span>#누수탐지</span><span>#고압세척</span><span>#변기막힘</span><span>#CCTV관로검사</span>
    </div>
  </div>
</section>
"""

TRUST = """<section class="section section--off" aria-labelledby="trust-h">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Why Speed Plumbing</span>
      <h2 id="trust-h">상업시설이 스피드를 선택하는 이유</h2>
      <p class="lead">한 번의 누수, 한 번의 막힘이 곧 영업 손실인 현장. 그래서 우리는 속도와 책임을 동시에 약속합니다.</p>
    </div>
    <div class="trust-grid">
      <div class="trust-card"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg></div><h3>24시간 긴급 출동</h3><p>야간·휴일에도 접수 즉시 가까운 작업팀이 출동합니다. 영업을 멈추지 않습니다.</p></div>
      <div class="trust-card"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div><h3>선견적 후작업</h3><p>현장 진단 후 비용을 먼저 안내합니다. 사전 협의 없는 추가금은 청구하지 않습니다.</p></div>
      <div class="trust-card"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M9 21v-6h6v6"/></svg></div><h3>상업시설 전문</h3><p>호텔·상가·빌딩의 대형 배관과 설비를 다루는 전문 인력과 장비를 갖추었습니다.</p></div>
      <div class="trust-card"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/></svg></div><h3>전국 네트워크</h3><p>전국 시·도 작업망으로 어디서든 빠르게 연결되는 출동 체계를 운영합니다.</p></div>
    </div>
  </div>
</section>
"""

SERVICE_GRID = """<section class="section" aria-labelledby="svc-h">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Services</span>
      <h2 id="svc-h">한눈에 보는 배관 서비스</h2>
      <p class="lead">상업시설에서 가장 많이 발생하는 배관 문제를 전문 장비로 신속하게 해결합니다.</p>
    </div>
    <div class="service-grid">
      <a class="service-card" href="/service/sewer-clog.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h18"/><path d="M6 7v9a3 3 0 0 0 3 3h6a3 3 0 0 0 3-3V7"/><path d="M9 11v3M15 11v3"/></svg></div><h3>하수구막힘</h3><p>역류·악취·배수 지연을 근본 원인부터 해결.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/plumbing.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h7v4H4z"/><path d="M11 9h5a3 3 0 0 1 3 3v8"/><path d="M16 20h6"/></svg></div><h3>배관공사</h3><p>노후관 교체·신설·증설 등 종합 배관 시공.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/leak-detection.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg></div><h3>누수탐지</h3><p>벽·바닥 철거 없이 비파괴 정밀 탐지.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/high-pressure.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h6"/><path d="M9 9l4 3-4 3z"/><path d="M14 7v10M18 5v14"/></svg></div><h3>고압세척</h3><p>관 내부 기름때·스케일을 고압수로 완전 제거.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/cctv.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/></svg></div><h3>CCTV 관로검사</h3><p>배관 내부를 영상으로 진단해 원인 특정.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/sewer-clog.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="2" width="12" height="9" rx="2"/><path d="M9 11v9a3 3 0 0 0 6 0v-9"/></svg></div><h3>변기·싱크대막힘</h3><p>변기·싱크대·바닥배수구 막힘 즉시 처리.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/plumbing.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v6"/><path d="M5 8h14l-1 12a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2z"/></svg></div><h3>정화조·동파</h3><p>정화조 관리·청소 및 겨울철 동파 복구.</p><span class="more">자세히 →</span></a>
      <a class="service-card" href="/service/plumbing.html"><div class="ico-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 7l3 3"/><path d="M3 21l3-1 11-11-2-2L4 18z"/><path d="M17 4l3 3"/></svg></div><h3>배관 리모델링</h3><p>상가·사무실 인테리어 배관 재배치·정비.</p><span class="more">자세히 →</span></a>
    </div>
  </div>
</section>
"""

AREA_BLOCK = """<section class="section section--off" aria-labelledby="area-h">
  <div class="container area-block">
    <div>
      <span class="eyebrow">Nationwide</span>
      <h2 id="area-h">우리 지역, 가까운 작업팀을 바로 찾으세요</h2>
      <p class="lead">스피드 배관공사는 전국 17개 시·도 네트워크로 운영됩니다. 호텔·상가·빌딩이 밀집한 주요 도시는 물론, 인근 시·군·구까지 신속하게 출동합니다. 지역을 선택하면 해당 지역의 시공사례와 연락처를 확인할 수 있습니다.</p>
      <p><a class="btn btn--secondary" href="/area/">전국 지역 전체 보기</a></p>
    </div>
    <nav class="region-grid" aria-label="시도 바로가기">
      <a href="/area/seoul/">서울</a><a href="/area/busan/">부산</a><a href="/area/daegu/">대구</a><a href="/area/incheon/">인천</a>
      <a href="/area/gwangju/">광주</a><a href="/area/daejeon/">대전</a><a href="/area/ulsan/">울산</a><a href="/area/sejong/">세종</a>
      <a href="/area/gyeonggi/">경기</a><a href="/area/gangwon/">강원</a><a href="/area/chungbuk/">충북</a><a href="/area/chungnam/">충남</a>
      <a href="/area/jeonbuk/">전북</a><a href="/area/jeonnam/">전남</a><a href="/area/gyeongbuk/">경북</a><a href="/area/gyeongnam/">경남</a><a href="/area/jeju/">제주</a>
    </nav>
  </div>
</section>
"""

STEPS = """<section class="section" aria-labelledby="step-h">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">Process</span><h2 id="step-h">접수부터 A/S까지, 투명한 5단계</h2><p class="lead">모든 과정에서 비용과 작업 범위를 명확히 공유합니다.</p></div>
    <ol class="steps">
      <li class="step"><div class="num">01</div><h3>전화 접수</h3><p>증상과 위치를 알려주시면 가까운 팀을 즉시 배정합니다.</p></li>
      <li class="step"><div class="num">02</div><h3>신속 출동</h3><p>전용 장비를 갖춘 작업팀이 현장으로 출동합니다.</p></li>
      <li class="step"><div class="num">03</div><h3>진단·견적</h3><p>원인을 진단하고 비용을 먼저 안내, 동의 후 진행합니다.</p></li>
      <li class="step"><div class="num">04</div><h3>전문 작업</h3><p>전문 장비로 신속·정확하게 작업하고 현장을 정리합니다.</p></li>
      <li class="step"><div class="num">05</div><h3>점검·A/S</h3><p>마무리 점검과 사후 보증으로 재발을 관리합니다.</p></li>
    </ol>
  </div>
</section>
"""

PRICE_PREVIEW = """<section class="section section--off" aria-labelledby="price-h">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Pricing</span><h2 id="price-h">대표 요금 미리보기</h2><p class="lead">아래는 일반적인 참고 단가이며, 현장 상황에 따라 달라집니다. 정확한 비용은 무료 상담으로 안내해 드립니다.</p></div>
    <div class="price-table-wrap"><table class="price-table">
      <caption>※ 부가세 별도 · 현장 진단 후 선견적 제공</caption>
      <thead><tr><th scope="col">서비스 항목</th><th scope="col">작업 범위</th><th scope="col">예상 요금</th></tr></thead>
      <tbody>
        <tr><td>하수구막힘</td><td>일반 관로 뚫음 (스프링/관통)</td><td class="unit">5만원~</td></tr>
        <tr><td>변기·싱크대막힘</td><td>이물질 제거·압력 관통</td><td class="unit">4만원~</td></tr>
        <tr><td>고압세척</td><td>관 내부 기름때·스케일 세척 (m당)</td><td class="unit">별도 산정</td></tr>
        <tr><td>누수탐지</td><td>비파괴 정밀 탐지 (지점당)</td><td class="unit">10만원~</td></tr>
        <tr><td>CCTV 관로검사</td><td>관 내부 영상 진단</td><td class="unit">8만원~</td></tr>
        <tr><td>배관공사</td><td>노후관 교체·신설</td><td class="unit">현장 견적</td></tr>
      </tbody>
    </table></div>
    <p class="price-note">상업시설 정기 관리 계약 시 별도 할인 및 우선 출동이 적용됩니다. · <a href="/price.html">전체 요금표 보기</a></p>
  </div>
</section>
"""

def case_grid(more=True):
    btn = '<p style="text-align:center;margin-top:32px;"><a class="btn btn--secondary" href="/cases.html">시공사례 전체보기</a></p>' if more else ""
    return f"""<section class="section" aria-labelledby="case-h">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">Before / After</span><h2 id="case-h">실제 시공 사례</h2><p class="lead">막힘과 누수, 결과로 증명합니다.</p></div>
    <div class="case-grid">
      <article class="case-card"><div class="ba"><figure class="before"><img src="/assets/img/case1.svg" alt="강남 호텔 주방 하수구 막힘 작업 전 상태" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case1-after.svg" alt="강남 호텔 주방 하수구 고압세척 후 깨끗해진 배관" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">호텔 · 하수구막힘</span><h3>강남 호텔 주방 배관 고압세척</h3><p>기름때 누적으로 반복되던 역류를 고압세척으로 근본 해결.</p></div></article>
      <article class="case-card"><div class="ba"><figure class="before"><img src="/assets/img/case2.svg" alt="상가 화장실 누수로 천장에 얼룩이 생긴 작업 전 상태" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case2-after.svg" alt="상가 화장실 누수 지점 보수 후 복구된 천장" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">상가 · 누수탐지</span><h3>성남 상가 천장 누수 비파괴 탐지</h3><p>철거 없이 누수 지점을 특정해 복구 범위와 비용을 최소화.</p></div></article>
      <article class="case-card"><div class="ba"><figure class="before"><img src="/assets/img/case3.svg" alt="오피스빌딩 지하 배관 노후로 부식된 작업 전 상태" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case3-after.svg" alt="오피스빌딩 지하 노후 배관 교체 후 새 배관" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">빌딩 · 배관공사</span><h3>해운대 오피스빌딩 지하 노후관 교체</h3><p>부식이 진행된 메인 배관을 야간 작업으로 무중단 교체.</p></div></article>
    </div>
    {btn}
  </div>
</section>
"""

REVIEWS = """<section class="section section--off" aria-labelledby="review-h">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">Reviews</span><h2 id="review-h">고객이 남긴 후기</h2><p class="lead">네이버 플레이스에서 더 많은 실제 후기를 확인하세요.</p></div>
    <div class="review-grid">
      <article class="review-card"><div class="stars" aria-label="별점 5점">★★★★★</div><blockquote>“야간에 호텔 객실 층 배수가 막혔는데 30분 만에 오셔서 영업에 지장 없이 해결해주셨어요. 견적도 먼저 정확히 알려주셔서 믿음이 갔습니다.”</blockquote><div class="review-meta"><span class="review-avatar">김</span><div><div class="who">김OO 지배인</div><div class="where">서울 강남 · 호텔</div></div></div></article>
      <article class="review-card"><div class="stars" aria-label="별점 5점">★★★★★</div><blockquote>“상가 화장실 누수 원인을 다른 곳에선 못 찾았는데, 벽 안 뜯고 정확히 짚어주셔서 복구비를 크게 아꼈습니다. 세금계산서도 깔끔하게 처리됐어요.”</blockquote><div class="review-meta"><span class="review-avatar">이</span><div><div class="who">이OO 점주</div><div class="where">경기 성남 · 상가</div></div></div></article>
      <article class="review-card"><div class="stars" aria-label="별점 5점">★★★★★</div><blockquote>“빌딩 지하 배관 교체를 야간 무중단으로 진행해 주셔서 입주사 불만 없이 끝냈습니다. 정기 관리까지 맡기기로 했어요.”</blockquote><div class="review-meta"><span class="review-avatar">박</span><div><div class="who">박OO 관리소장</div><div class="where">부산 해운대 · 오피스빌딩</div></div></div></article>
    </div>
    <p style="text-align:center;margin-top:32px;"><a class="btn btn--secondary" href="/review.html">고객후기 전체보기</a> &nbsp; <a class="btn btn--primary" href="https://map.naver.com/" rel="noopener" target="_blank">네이버 플레이스에서 보기</a></p>
  </div>
</section>
"""

HOME_FAQ = f"""<section class="section" aria-labelledby="faq-h">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">FAQ</span><h2 id="faq-h">자주 묻는 질문</h2></div>
    <div class="faq-list">
{faq_html(FAQ_ITEMS)}    </div>
    <p style="text-align:center;margin-top:28px;"><a href="/faq.html">자주 묻는 질문 더 보기 →</a></p>
  </div>
</section>
"""

HOME_BODY = ("<main>\n" + HERO + TRUST + SERVICE_GRID + AREA_BLOCK + STEPS +
             PRICE_PREVIEW + case_grid() + REVIEWS + HOME_FAQ + bottom_cta() + "</main>\n")

page("index.html",
     "스피드 배관공사 | 호텔·상가·빌딩 상업시설 전문 배관 · 24시간 출동",
     "호텔·상가·오피스빌딩 등 상업시설 전문 B2B 배관 파트너 스피드 배관공사. 하수구막힘·배관공사·누수탐지·고압세척을 24시간 신속 출동으로 해결합니다. 선견적 후작업, 추가금 없음, 전국 네트워크.",
     S + "/",
     HOME_BODY,
     jsonld=HOME_JSONLD + faq_jsonld(FAQ_ITEMS),
     og_title="스피드 배관공사 | 상업시설 전문 24시간 배관 파트너",
     og_desc="호텔·상가·빌딩 배관, 멈추지 않는 신속함. 하수구막힘·배관공사·누수탐지·고압세척 24시간 출동.")


# ===========================================================================
# 공통: 페이지 히어로 + 빵부스러기
# ===========================================================================
def phero(eyebrow, h1, sub, crumbs):
    items = ""
    for i, (label, url) in enumerate(crumbs):
        if url and i < len(crumbs) - 1:
            items += f'<li><a href="{url}">{label}</a></li>'
        else:
            items += f'<li><span aria-current="page">{label}</span></li>'
    return f"""<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="현재 위치"><ol>{items}</ol></nav>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p>{sub}</p>
  </div>
</section>
"""

# ===========================================================================
# 서비스 상세 (증상/원인 → 작업방법 → 사용장비 → 예상요금 → 시공사례 → CTA)
# ===========================================================================
def service_page(slug, name, eyebrow, h1, hero_sub, title, desc,
                 symptoms, causes, methods, equipment, price_rows,
                 service_faq, related):
    crumbs = [("홈", "/"), ("서비스안내", "/service/"), (name, None)]
    sym = "".join(f"<li>{x}</li>" for x in symptoms)
    cau = "".join(f"<li>{x}</li>" for x in causes)
    met = "".join(f"<li><strong>{t}.</strong> {d}</li>" for t, d in methods)
    eq = "".join(f"<span>{x}</span>" for x in equipment)
    pr = "".join(f"<tr><td>{a}</td><td>{b}</td><td class='unit'>{c}</td></tr>" for a, b, c in price_rows)
    rel = "".join(f'<a class="link-card" href="{u}"><h3>{n}</h3><p>{p}</p></a>' for n, p, u in related)
    faq_block = ""
    faq_ld = ""
    if service_faq:
        faq_block = f"""<section class="section section--off" aria-labelledby="sfaq-h">
  <div class="container">
    <div class="section-head center"><span class="eyebrow">FAQ</span><h2 id="sfaq-h">{name} 자주 묻는 질문</h2></div>
    <div class="faq-list">
{faq_html(service_faq)}    </div>
  </div>
</section>
"""
        faq_ld = faq_jsonld(service_faq)
    body = f"""{phero(eyebrow, h1, hero_sub, crumbs)}
<main>
<section class="section">
  <div class="container layout-sidebar">
    <div class="prose">
      <p class="lead">{hero_sub}</p>

      <h2>이런 증상이라면 {name} 점검이 필요합니다</h2>
      <ul class="ticks">{sym}</ul>

      <h2>주요 원인</h2>
      <ul class="ticks">{cau}</ul>

      <h2>작업 방법</h2>
      <ol style="padding-left:20px;display:flex;flex-direction:column;gap:10px;">{met}</ol>

      <h2>사용 장비</h2>
      <div class="chips">{eq}</div>

      <h2>예상 요금</h2>
      <div class="price-table-wrap"><table class="price-table">
        <caption>※ 부가세 별도 · 현장 진단 후 선견적 제공</caption>
        <thead><tr><th scope="col">항목</th><th scope="col">작업 범위</th><th scope="col">예상 요금</th></tr></thead>
        <tbody>{pr}</tbody>
      </table></div>
      <p class="price-note">현장 상황(관 길이·접근성·상태)에 따라 비용이 달라질 수 있어 정확한 금액은 무료 상담으로 안내드립니다.</p>

      <h2>관련 서비스</h2>
      <div class="card-grid">{rel}</div>
    </div>
    {SIDEBAR}
  </div>
</section>
{case_grid()}
{faq_block}
{bottom_cta()}
</main>
"""
    page(f"service/{slug}.html", title, desc, f"{S}/service/{slug}.html", body,
         jsonld=breadcrumb_jsonld(crumbs) + faq_ld)


service_page(
    "sewer-clog", "하수구막힘", "Service · 하수구막힘",
    "하수구막힘, 역류 전에 근본부터 뚫습니다",
    "주방·화장실·바닥 배수구의 하수구막힘을 스프링·관통기·고압세척으로 신속 해결하고, CCTV로 원인을 진단해 재발을 막습니다.",
    "하수구막힘 | 상업시설 배관 막힘 24시간 출동 - 스피드 배관공사",
    "하수구막힘·역류·악취를 24시간 출동으로 해결합니다. 호텔·상가·빌딩 등 상업시설의 반복되는 하수구막힘을 CCTV 진단과 고압세척으로 근본 해결. 선견적 후작업.",
    ["물이 천천히 빠지거나 역류한다", "배수구에서 악취가 올라온다", "여러 배수구가 동시에 막힌다", "변기 물이 잘 내려가지 않는다"],
    ["기름때·음식물 찌꺼기 누적 (주방)", "머리카락·이물질 엉킴 (화장실)", "배관 구배 불량·이물질 투입", "노후관 내부 스케일 침착"],
    [("증상 확인 및 진단", "막힘 위치와 정도를 파악하고 필요 시 CCTV로 관 내부를 확인합니다."),
     ("관통 작업", "전동 스프링·관통기로 막힘을 1차 제거합니다."),
     ("고압세척", "기름때·스케일이 원인이면 고압수로 관 벽을 세척해 흐름을 회복합니다."),
     ("점검 및 재발 방지 안내", "배수 상태를 확인하고 정기 관리·구배 개선 등을 제안합니다.")],
    ["전동 스프링", "관통기(오거)", "고압세척기", "CCTV 관로카메라", "악취 차단 트랩"],
    [("일반 하수구", "스프링/관통 1개소", "5만원~"),
     ("주방 배관", "기름때 고압세척 병행", "별도 산정"),
     ("바닥 배수구", "이물질 제거", "4만원~"),
     ("반복 막힘", "CCTV 진단 + 근본 처리", "현장 견적")],
    [("하수구막힘은 왜 자꾸 반복되나요?", "관 내부에 기름때나 스케일이 얇게 남으면 다시 빠르게 쌓입니다. 일시적 뚫음이 아니라 고압세척으로 관 벽까지 세척하고 CCTV로 구배·파손 여부를 확인하면 재발을 크게 줄일 수 있습니다."),
     ("영업 중에도 작업이 가능한가요?", "네. 소음·냄새를 최소화하는 장비로 영업에 지장이 적게 작업하며, 필요 시 야간·새벽 시간대 작업도 조율합니다.")],
    [("고압세척", "관 내부 기름때·스케일 완전 제거", "/service/high-pressure.html"),
     ("CCTV 관로검사", "막힘 원인을 영상으로 진단", "/service/cctv.html"),
     ("누수탐지", "막힘과 함께 의심되는 누수 점검", "/service/leak-detection.html")],
)

service_page(
    "plumbing", "배관공사", "Service · 배관공사",
    "노후관 교체부터 신설까지, 상업시설 배관공사",
    "호텔·상가·빌딩의 급수·배수·오수 배관을 교체·신설·증설합니다. 영업 중단을 최소화하는 야간·단계 시공으로 진행합니다.",
    "배관공사 | 상업시설 급수·배수 배관 교체·신설 - 스피드 배관공사",
    "상업시설 배관공사 전문. 노후관 교체, 급수·배수·오수 배관 신설·증설, 누수 보수까지. 야간 무중단 시공과 선견적으로 안전하게 진행합니다.",
    ["배관이 노후되어 부식·누수가 잦다", "수압이 약하거나 배수가 원활하지 않다", "리모델링으로 배관 재배치가 필요하다", "증축·용도 변경으로 배관 증설이 필요하다"],
    ["설치 후 15년 이상 경과한 금속관 부식", "잦은 막힘으로 인한 관 손상", "동결·외부 충격에 의한 파손", "설계 용량 초과·구배 불량"],
    [("현장 실측 및 설계", "배관 경로·용량·자재를 진단하고 시공안과 견적을 제시합니다."),
     ("자재 준비 및 일정 협의", "PB·스테인리스·주철 등 용도에 맞는 자재를 선정하고 무중단 일정을 조율합니다."),
     ("배관 교체·신설 시공", "구간별 차단·우회로 영업 영향을 최소화하며 시공합니다."),
     ("수압·누수 테스트 및 마감", "통수·가압 테스트로 누수를 확인하고 현장을 복구·정리합니다.")],
    ["배관 절단·나사 가공기", "동관·PB 압착공구", "전기 융착기", "가압 테스트 펌프", "관 검사 카메라"],
    [("노후관 교체", "구간·자재별", "현장 견적"),
     ("급수 배관 신설", "용량·경로별", "현장 견적"),
     ("배수·오수 배관", "구배 재시공 포함", "현장 견적"),
     ("부분 보수", "누수·파손 구간", "10만원~")],
    [("영업을 멈추지 않고 배관을 교체할 수 있나요?", "구간별 차단과 우회 배관, 야간·새벽 시공을 활용해 영업 중단을 최소화합니다. 호텔·상가의 운영 일정에 맞춰 단계 시공을 계획합니다."),
     ("어떤 자재를 사용하나요?", "용도와 수질·압력 조건에 맞춰 스테인리스, PB, 동관, 주철 등을 선정합니다. 견적 시 자재 등급과 보증 내용을 함께 안내합니다.")],
    [("누수탐지", "교체 전 누수 위치 정밀 확인", "/service/leak-detection.html"),
     ("CCTV 관로검사", "배관 상태를 영상으로 진단", "/service/cctv.html"),
     ("하수구막힘", "배수 불량 동반 시 함께 처리", "/service/sewer-clog.html")],
)

service_page(
    "leak-detection", "누수탐지", "Service · 누수탐지",
    "벽을 뜯지 않고 누수 지점을 찾습니다",
    "청음·열화상·가스 탐지 등 비파괴 장비로 누수 위치를 정확히 특정합니다. 불필요한 철거를 줄여 복구 비용과 시간을 아낍니다.",
    "누수탐지 | 비파괴 정밀 누수 탐지 - 스피드 배관공사",
    "벽·바닥 철거 없이 누수 위치를 찾는 비파괴 누수탐지. 청음식 탐지기·열화상 카메라·가스 탐지로 호텔·상가·빌딩의 숨은 누수를 정확히 진단합니다.",
    ["수도 사용이 없는데 계량기가 돈다", "벽·천장·바닥에 물 얼룩·곰팡이가 있다", "원인 모를 수도 요금 급증", "아래층으로 물이 새 분쟁이 우려된다"],
    ["배관 이음부 노화·균열", "콘크리트 매립 배관 부식", "외부 충격·동결에 의한 미세 파손", "방수층 손상으로 인한 침투"],
    [("현장 청취 및 1차 점검", "누수 정황과 사용 패턴을 확인하고 의심 구간을 좁힙니다."),
     ("비파괴 정밀 탐지", "청음·열화상·가스 추적으로 누수 지점을 특정합니다."),
     ("위치 표시 및 복구안 제시", "최소 철거 범위를 표시하고 보수 방법·비용을 안내합니다."),
     ("보수 및 재점검", "보수 후 가압 테스트로 누수 해소를 확인합니다.")],
    ["청음식 누수탐지기", "열화상 카메라", "추적가스 탐지기", "관로 내시경", "수압 측정기"],
    [("누수 정밀 탐지", "지점당", "10만원~"),
     ("열화상 진단", "구역별", "별도 산정"),
     ("탐지+보수", "패키지", "현장 견적"),
     ("누수 보수", "이음부·구간", "현장 견적")],
    [("정말 벽을 안 뜯고 찾을 수 있나요?", "대부분의 누수는 청음·열화상·가스 탐지로 위치를 특정할 수 있어 철거를 최소화합니다. 다만 매립 깊이나 구조에 따라 일부 확인 작업이 필요할 수 있으며, 사전에 안내드립니다."),
     ("탐지만 받고 보수는 따로 맡겨도 되나요?", "가능합니다. 탐지 결과 리포트와 위치 표시를 제공하므로 자체 보수나 타 업체 보수에도 활용할 수 있습니다.")],
    [("배관공사", "탐지 후 누수 구간 보수·교체", "/service/plumbing.html"),
     ("CCTV 관로검사", "배수관 내부 파손 확인", "/service/cctv.html"),
     ("고압세척", "보수 전 관 내부 세척", "/service/high-pressure.html")],
)

service_page(
    "high-pressure", "고압세척", "Service · 고압세척",
    "관 벽까지 새것처럼, 고압세척",
    "고압수로 관 내부의 기름때·슬러지·스케일을 제거해 배수 흐름을 회복합니다. 주방·정화조·오수관 등 누적 오염에 효과적입니다.",
    "고압세척 | 배관 내부 기름때·스케일 제거 - 스피드 배관공사",
    "고압세척으로 호텔·상가 주방 배관과 오수관의 기름때·스케일을 완전 제거합니다. 반복되는 하수구막힘의 근본 원인을 해결하는 정기 관리 서비스.",
    ["주기적으로 배수가 느려진다", "주방 배관에서 기름 냄새가 난다", "막힘이 짧은 주기로 반복된다", "오수·정화조 관로에 슬러지가 쌓였다"],
    ["식용유·유지방의 관 벽 침착", "세제·미네랄 스케일 누적", "장기 미세척으로 인한 협착", "구배 불량으로 침전물 정체"],
    [("관로 상태 진단", "필요 시 CCTV로 오염 정도와 구간을 확인합니다."),
     ("고압세척 시공", "회전·직진 노즐을 사용해 관 벽의 오염을 박리·배출합니다."),
     ("배출물 처리", "세척으로 떨어진 슬러지를 안전하게 수거·처리합니다."),
     ("정기 관리 제안", "오염 주기를 고려한 정기 세척 주기를 제안합니다.")],
    ["고압세척기(워터젯)", "회전·직진 노즐", "릴 호스 시스템", "CCTV 관로카메라", "슬러지 수거 장비"],
    [("주방 배관 세척", "구간·길이별(m당)", "별도 산정"),
     ("오수·정화조 관로", "현장 상태별", "현장 견적"),
     ("정기 관리 계약", "월/분기 단위", "할인 적용"),
     ("CCTV 진단 병행", "세척 전후 비교", "8만원~")],
    [("얼마나 자주 세척하면 좋나요?", "주방 사용량이 많은 호텔·식당은 분기 1회, 일반 상가는 반기~연 1회를 권장합니다. 사용 패턴을 보고 적정 주기를 함께 정해 드립니다."),
     ("세척하면 막힘이 정말 줄어드나요?", "관 벽의 기름때·스케일이 제거되면 유효 단면이 회복되어 막힘 빈도가 크게 줄어듭니다. 정기 관리와 병행하면 효과가 오래 유지됩니다.")],
    [("하수구막힘", "막힘 발생 시 즉시 관통", "/service/sewer-clog.html"),
     ("CCTV 관로검사", "세척 효과를 영상으로 확인", "/service/cctv.html"),
     ("배관공사", "세척으로 회복 어려운 노후관 교체", "/service/plumbing.html")],
)

service_page(
    "cctv", "CCTV 관로검사", "Service · CCTV 관로검사",
    "배관 속을 눈으로 확인하는 CCTV 진단",
    "관로 전용 카메라로 배관 내부를 촬영해 막힘·파손·역구배·이물질을 정확히 진단합니다. 추측이 아닌 근거로 작업을 결정합니다.",
    "CCTV 관로검사 | 배관 내부 영상 진단 - 스피드 배관공사",
    "CCTV 관로검사로 배관 내부의 막힘·균열·역구배·이물질을 영상으로 진단합니다. 반복되는 하수구막힘과 누수의 원인을 정확히 찾아 근본 해결합니다.",
    ["막힘·누수가 반복되는데 원인을 모른다", "배관 매입 위치·경로를 확인하고 싶다", "인수인계·하자 점검 근거가 필요하다", "공사 전 배관 상태를 진단하고 싶다"],
    ["관 내부 균열·이음부 이탈", "역구배·처짐으로 인한 정체", "이물질·뿌리 침입", "노후로 인한 협착"],
    [("카메라 투입", "관경에 맞는 관로 카메라를 배관에 투입합니다."),
     ("내부 촬영·진단", "막힘·파손·구배 상태를 실시간 영상으로 확인합니다."),
     ("위치 측정", "문제 지점의 거리·깊이를 측정해 위치를 특정합니다."),
     ("리포트 제공", "영상과 진단 결과를 바탕으로 보수안을 제안합니다.")],
    ["관로 CCTV 카메라", "거리 측정 시스템", "자주식 카메라(대형관)", "위치 추적 송신기", "영상 기록 장비"],
    [("관로 영상 진단", "구간별", "8만원~"),
     ("위치 측정 포함", "거리·깊이 측정", "별도 산정"),
     ("진단 리포트", "영상·소견 제공", "포함"),
     ("공사 전 진단", "시공 견적 연계", "현장 견적")],
    [("검사 영상이나 결과를 받을 수 있나요?", "네. 촬영 영상과 문제 지점, 소견을 정리해 제공합니다. 하자 점검·인수인계·보험 청구 근거로도 활용할 수 있습니다."),
     ("어떤 배관까지 검사가 가능한가요?", "소형 생활배관부터 대형 오수·우수관까지 관경에 맞는 카메라로 검사합니다. 자주식 카메라로 긴 구간도 진단 가능합니다.")],
    [("하수구막힘", "진단 후 막힘 즉시 처리", "/service/sewer-clog.html"),
     ("고압세척", "오염 구간 고압 세척", "/service/high-pressure.html"),
     ("배관공사", "파손 구간 교체·보수", "/service/plumbing.html")],
)


# ===========================================================================
# 서비스 인덱스
# ===========================================================================
SVC_LIST = [
    ("하수구막힘", "역류·악취·배수 지연을 근본 원인부터 해결합니다.", "/service/sewer-clog.html"),
    ("배관공사", "노후관 교체·신설·증설 등 종합 배관 시공.", "/service/plumbing.html"),
    ("누수탐지", "벽·바닥 철거 없이 비파괴 정밀 탐지.", "/service/leak-detection.html"),
    ("고압세척", "관 내부 기름때·스케일을 고압수로 완전 제거.", "/service/high-pressure.html"),
    ("CCTV 관로검사", "배관 내부를 영상으로 진단해 원인 특정.", "/service/cctv.html"),
    ("변기·싱크대막힘", "변기·싱크대·바닥배수구 막힘 즉시 처리.", "/service/sewer-clog.html"),
    ("정화조·동파", "정화조 관리·청소 및 겨울철 동파 복구.", "/service/plumbing.html"),
    ("배관 리모델링", "상가·사무실 인테리어 배관 재배치·정비.", "/service/plumbing.html"),
]
svc_cards = "".join(f'<a class="link-card" href="{u}"><h3>{n}</h3><p>{p}</p></a>' for n, p, u in SVC_LIST)
svc_body = f"""{phero("Services", "서비스안내", "상업시설에서 발생하는 모든 배관 문제를 한 곳에서 해결합니다. 각 서비스를 선택해 자세한 작업 방법과 예상 요금을 확인하세요.", [("홈","/"),("서비스안내",None)])}
<main>
<section class="section">
  <div class="container">
    <div class="card-grid">{svc_cards}</div>
  </div>
</section>
{bottom_cta()}
</main>
"""
page("service/index.html", "서비스안내 | 하수구막힘·배관공사·누수탐지·고압세척 - 스피드 배관공사",
     "스피드 배관공사의 전체 서비스. 하수구막힘, 배관공사, 누수탐지, 고압세척, CCTV 관로검사 등 상업시설 전문 배관 서비스를 한눈에 확인하세요.",
     S + "/service/", svc_body,
     jsonld=breadcrumb_jsonld([("홈","/"),("서비스안내","/service/")]))

# ===========================================================================
# 지역 허브
# ===========================================================================
def area_index():
    SIDO = ["서울특별시","부산광역시","대구광역시","인천광역시","광주광역시","대전광역시","울산광역시",
            "세종특별자치시","경기도","강원특별자치도","충청북도","충청남도","전북특별자치도","전라남도",
            "경상북도","경상남도","제주특별자치도"]
    links = {"서울특별시":"/area/seoul/","부산광역시":"/area/busan/","대구광역시":"/area/daegu/",
             "인천광역시":"/area/incheon/","광주광역시":"/area/gwangju/","대전광역시":"/area/daejeon/",
             "울산광역시":"/area/ulsan/","세종특별자치시":"/area/sejong/","경기도":"/area/gyeonggi/",
             "강원특별자치도":"/area/gangwon/","충청북도":"/area/chungbuk/","충청남도":"/area/chungnam/",
             "전북특별자치도":"/area/jeonbuk/","전라남도":"/area/jeonnam/","경상북도":"/area/gyeongbuk/",
             "경상남도":"/area/gyeongnam/","제주특별자치도":"/area/jeju/"}
    cards = ""
    for s in SIDO:
        u = links.get(s, "/area/")
        cards += f'<a class="link-card" href="{u}"><h3>{s}</h3><p>{s} 전역 상업시설 배관 출동</p></a>'
    body = f"""{phero("Nationwide", "지역별 서비스", "스피드 배관공사는 전국 17개 시·도에서 호텔·상가·빌딩 배관 서비스를 제공합니다. 지역을 선택하면 해당 지역의 출동 안내와 시공사례를 확인할 수 있습니다.", [("홈","/"),("지역별 서비스",None)])}
<main>
<section class="section">
  <div class="container">
    <div class="card-grid">{cards}</div>
    <p class="price-note" style="margin-top:24px;">※ 읍·면·동 단위 페이지는 별도로 생성하지 않으며, 각 시·군·구 페이지 내 ‘서비스 가능 지역’ 목록으로 안내합니다.</p>
  </div>
</section>
{bottom_cta()}
</main>
"""
    page("area/index.html", "지역별 서비스 | 전국 17개 시·도 상업시설 배관 - 스피드 배관공사",
         "스피드 배관공사 전국 서비스 지역 안내. 서울·부산·경기 등 17개 시·도에서 호텔·상가·빌딩 배관, 하수구막힘, 누수탐지를 24시간 출동으로 해결합니다.",
         S + "/area/", body,
         jsonld=breadcrumb_jsonld([("홈","/"),("지역별 서비스","/area/")]))
area_index()


def sido_page(slug, name, short, intro, districts, district_links, cases_html, phone_note):
    crumbs = [("홈","/"),("지역별 서비스","/area/"),(name, None)]
    dcards = ""
    for d in districts:
        u = district_links.get(d)
        if u:
            dcards += f'<a class="link-card" href="{u}"><h3>{d}</h3><p>{name} {d} 배관·하수구막힘 출동</p></a>'
        else:
            dcards += f'<div class="link-card" style="opacity:.85"><h3>{d}</h3><p>{name} {d} 출동 가능</p></div>'
    body = f"""{phero(f"{name} 서비스", f"{name} 배관·하수구막힘 24시간 출동", intro, crumbs)}
<main>
<section class="section">
  <div class="container layout-sidebar">
    <div class="prose">
      <h2>{name} 상업시설 배관, 스피드가 함께합니다</h2>
      <p>{short}</p>
      <p>{intro}</p>

      <h2>{name} 시·군·구 서비스</h2>
      <p>아래 지역을 선택하면 해당 시·군·구의 출동 안내를 확인할 수 있습니다.</p>
      <div class="card-grid">{dcards}</div>

      <h2>{name} 시공 사례</h2>
      {cases_html}

      <h2>이런 현장에서 자주 불러주십니다</h2>
      <ul class="ticks">
        <li>호텔·모텔·숙박시설 주방 및 객실 층 배관</li>
        <li>상가·식당 밀집 지역의 기름때 하수구막힘</li>
        <li>오피스빌딩 지하 메인 배관 누수·교체</li>
      </ul>
    </div>
    <aside class="sidebar-card">
      <h3>{name} 상담</h3>
      <p>{phone_note}</p>
      <a class="phone-big" href="tel:1577-0000">1577-0000</a>
      <p style="margin-bottom:18px;">카카오톡 상담 @스피드배관</p>
      <a class="btn btn--primary btn--block" href="tel:1577-0000">☎ 전화 상담</a>
      <a class="btn btn--ghost-light btn--block" href="/contact.html" style="margin-top:10px;">무료 견적 신청</a>
    </aside>
  </div>
</section>
{bottom_cta(h2=f"{name} 어디든, 지금 출동합니다")}
</main>
"""
    title = f"{name} 배관·하수구막힘·누수탐지 24시간 출동 - 스피드 배관공사"
    desc = f"{name} 상업시설 전문 배관 서비스. {name} 호텔·상가·빌딩의 하수구막힘, 배관공사, 누수탐지, 고압세척을 24시간 신속 출동으로 해결합니다. 선견적 후작업."
    page(f"area/{slug}/index.html", title, desc, f"{S}/area/{slug}/", body,
         jsonld=breadcrumb_jsonld(crumbs))


# --- 서울 ---
sido_page(
    "seoul", "서울특별시",
    "강남·중구·영등포 등 업무·상업 밀집 지역이 많은 서울은 야간에도 영업하는 시설이 많아 즉시 대응이 중요합니다. 스피드 배관공사는 서울 전역에 작업팀을 배치해 평균 30분 내 출동을 목표로 운영합니다.",
    "호텔·백화점·대형 상가가 밀집한 서울 도심 특성상 주방 기름때로 인한 하수구막힘과 노후 빌딩의 배관 누수 의뢰가 많습니다. 고압세척과 CCTV 진단을 기본으로 재발까지 관리합니다.",
    ["강남구","서초구","송파구","중구","종로구","영등포구","마포구","용산구","강서구","구로구","성동구","광진구"],
    {"강남구":"/area/seoul/gangnam.html"},
    """<article class="case-card" style="max-width:520px;"><div class="ba"><figure class="before"><img src="/assets/img/case1.svg" alt="서울 강남 호텔 주방 하수구 막힘 전" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case1-after.svg" alt="서울 강남 호텔 주방 고압세척 후" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">강남구 · 호텔</span><h3>강남 호텔 주방 배관 고압세척</h3><p>반복되던 역류를 고압세척으로 근본 해결.</p></div></article>""",
    "서울 전역 24시간 출동. 야간·새벽 긴급 작업 가능.")

# --- 경기 ---
sido_page(
    "gyeonggi", "경기도",
    "성남·수원·고양·용인 등 인구와 상권이 빠르게 성장하는 경기도는 대형 쇼핑몰과 신축 상가, 물류시설의 배관 수요가 많습니다. 권역별 작업팀으로 넓은 지역을 빠르게 커버합니다.",
    "신도시 상가의 주방 배관 막힘부터 노후 공장·물류센터의 대형 오수관 고압세척까지 폭넓게 대응합니다. 경기 남부·북부 권역에 작업팀을 분산 배치합니다.",
    ["성남시","수원시","용인시","고양시","부천시","안양시","화성시","남양주시","평택시","의정부시","파주시","김포시"],
    {},
    """<article class="case-card" style="max-width:520px;"><div class="ba"><figure class="before"><img src="/assets/img/case2.svg" alt="경기 성남 상가 천장 누수 전" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case2-after.svg" alt="경기 성남 상가 누수 보수 후" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">성남시 · 상가</span><h3>성남 상가 천장 누수 비파괴 탐지</h3><p>철거 없이 누수 지점을 특정해 복구비 최소화.</p></div></article>""",
    "경기 남부·북부 권역 24시간 출동.")

# --- 부산 ---
sido_page(
    "busan", "부산광역시",
    "해운대·서면·남포동 등 관광·상업 중심지가 많은 부산은 호텔과 식당가의 배관 관리 수요가 꾸준합니다. 해안가 특성상 노후 배관의 부식·누수 의뢰도 많습니다.",
    "관광 성수기 호텔의 객실 층 배수 긴급 대응과, 오래된 상가 건물의 노후관 교체를 함께 진행합니다. 해운대·중구·부산진구 권역에 작업팀을 배치합니다.",
    ["해운대구","부산진구","중구","동래구","남구","수영구","사하구","북구","금정구","연제구","사상구","기장군"],
    {},
    """<article class="case-card" style="max-width:520px;"><div class="ba"><figure class="before"><img src="/assets/img/case3.svg" alt="부산 해운대 오피스빌딩 지하 배관 노후 전" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case3-after.svg" alt="부산 해운대 오피스빌딩 배관 교체 후" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">해운대구 · 빌딩</span><h3>해운대 오피스빌딩 지하 노후관 교체</h3><p>부식 메인 배관을 야간 무중단 교체.</p></div></article>""",
    "부산 전역 24시간 출동. 해안가 노후 배관 전문.")


# --- 시군구 샘플: 서울 강남구 ---
def gangnam():
    crumbs = [("홈","/"),("지역별 서비스","/area/"),("서울특별시","/area/seoul/"),("강남구", None)]
    dong = ["역삼동","삼성동","대치동","논현동","청담동","압구정동","신사동","도곡동","개포동","일원동","수서동","세곡동"]
    tags = "".join(f"<span>{d}</span>" for d in dong)
    body = f"""{phero("강남구 서비스", "강남구 배관·하수구막힘 24시간 출동", "테헤란로 오피스빌딩과 청담·압구정 상권, 강남 일대 호텔까지 — 강남구 상업시설의 배관 문제를 즉시 해결합니다.", crumbs)}
<main>
<section class="section">
  <div class="container layout-sidebar">
    <div class="prose">
      <h2>강남구 상업시설 배관 전문</h2>
      <p>강남구는 테헤란로를 중심으로 오피스빌딩이 밀집하고, 청담·압구정·역삼 일대에 고급 상가와 식당, 호텔이 모여 있습니다. 영업 시간이 길고 야간 운영 시설이 많아 <strong>즉시 출동과 무중단 작업</strong>이 특히 중요한 지역입니다.</p>
      <p>스피드 배관공사는 강남 일대에 작업팀을 상시 배치해 주방 기름때 하수구막힘, 빌딩 노후관 누수, 정기 고압세척까지 한 번에 대응합니다. 선견적 후작업으로 비용을 먼저 확인하고 진행합니다.</p>

      <h2>강남구에서 자주 의뢰되는 작업</h2>
      <ul class="ticks">
        <li>테헤란로 오피스빌딩 지하 배관 누수탐지·교체</li>
        <li>청담·압구정 레스토랑 주방 배관 고압세척</li>
        <li>역삼·삼성동 호텔 객실 층 하수구막힘 긴급 대응</li>
        <li>상가 리모델링에 따른 배관 재배치</li>
      </ul>

      <h2>강남구 시공 사례</h2>
      <article class="case-card" style="max-width:520px;"><div class="ba"><figure class="before"><img src="/assets/img/case1.svg" alt="강남구 호텔 주방 하수구 막힘 전" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/case1-after.svg" alt="강남구 호텔 주방 고압세척 후" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">강남구 · 호텔</span><h3>강남 호텔 주방 배관 고압세척</h3><p>기름때 누적 역류를 근본 해결, 정기 관리 계약으로 전환.</p></div></article>

      <h2>강남구 서비스 가능 지역</h2>
      <p>아래 동네를 포함한 강남구 전역으로 출동합니다. (동 단위 별도 페이지는 운영하지 않습니다.)</p>
      <div class="tag-list">{tags}</div>
    </div>
    <aside class="sidebar-card">
      <h3>강남구 상담</h3>
      <p>강남 전역 24시간 출동. 야간·새벽 긴급 작업 가능.</p>
      <a class="phone-big" href="tel:1577-0000">1577-0000</a>
      <p style="margin-bottom:18px;">카카오톡 상담 @스피드배관</p>
      <a class="btn btn--primary btn--block" href="tel:1577-0000">☎ 전화 상담</a>
      <a class="btn btn--ghost-light btn--block" href="/contact.html" style="margin-top:10px;">무료 견적 신청</a>
    </aside>
  </div>
</section>
{bottom_cta(h2="강남구 어디든, 지금 출동합니다")}
</main>
"""
    page("area/seoul/gangnam.html",
         "강남구 배관·하수구막힘·누수탐지 24시간 출동 - 스피드 배관공사",
         "서울 강남구 상업시설 배관 전문. 테헤란로 오피스빌딩, 청담·압구정 상가, 강남 호텔의 하수구막힘·배관공사·누수탐지·고압세척을 24시간 출동으로 해결합니다.",
         S + "/area/seoul/gangnam.html", body, jsonld=breadcrumb_jsonld(crumbs))
gangnam()


# ===========================================================================
# 시공사례
# ===========================================================================
CASES = [
    ("호텔 · 하수구막힘","강남 호텔 주방 배관 고압세척","기름때 누적으로 반복되던 역류를 고압세척으로 근본 해결. 정기 관리 계약으로 전환.","case1.svg","case1-after.svg"),
    ("상가 · 누수탐지","성남 상가 천장 누수 비파괴 탐지","철거 없이 누수 지점을 특정해 복구 범위와 비용을 최소화.","case2.svg","case2-after.svg"),
    ("빌딩 · 배관공사","해운대 오피스빌딩 지하 노후관 교체","부식이 진행된 메인 배관을 야간 무중단으로 교체.","case3.svg","case3-after.svg"),
    ("식당 · 고압세척","서면 식당가 주방 오수관 고압세척","장기 미세척 오수관의 슬러지를 제거해 배수 정상화.","case1.svg","case1-after.svg"),
    ("오피스 · CCTV","여의도 오피스 배관 CCTV 진단","반복 막힘의 원인을 영상으로 특정해 정확히 보수.","case2.svg","case2-after.svg"),
    ("모텔 · 변기막힘","수원 숙박시설 객실 변기 긴급 처리","주말 야간 긴급 출동으로 영업 차질 없이 해결.","case3.svg","case3-after.svg"),
]
cards = ""
for tag, t, d, b, a in CASES:
    cards += f"""<article class="case-card"><div class="ba"><figure class="before"><img src="/assets/img/{b}" alt="{t} 작업 전" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure><figure class="after"><img src="/assets/img/{a}" alt="{t} 작업 후" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div><div class="case-body"><span class="case-tag">{tag}</span><h3>{t}</h3><p>{d}</p></div></article>"""
cases_body = f"""{phero("Before / After","시공사례","막힘과 누수, 결과로 증명합니다. 호텔·상가·빌딩 등 상업시설에서 진행한 실제 시공 사례를 소개합니다.",[("홈","/"),("시공사례",None)])}
<main>
<section class="section">
  <div class="container"><div class="case-grid">{cards}</div></div>
</section>
{bottom_cta()}
</main>
"""
page("cases.html","시공사례 | 상업시설 배관 Before/After - 스피드 배관공사",
     "스피드 배관공사 시공사례. 호텔 주방 고압세척, 상가 누수탐지, 빌딩 노후관 교체 등 상업시설 배관 작업의 Before/After를 확인하세요.",
     S + "/cases.html", cases_body, jsonld=breadcrumb_jsonld([("홈","/"),("시공사례","/cases.html")]))

# ===========================================================================
# 요금안내
# ===========================================================================
price_body = f"""{phero("Pricing","요금안내","현장 진단 후 선견적을 드리는 것이 원칙입니다. 아래 표는 참고용 단가이며, 관 길이·접근성·상태에 따라 달라집니다. 사전 협의 없는 추가금은 청구하지 않습니다.",[("홈","/"),("요금안내",None)])}
<main>
<section class="section">
  <div class="container prose" style="max-width:920px;">
    <h2>대표 서비스 요금</h2>
    <div class="price-table-wrap"><table class="price-table">
      <caption>※ 부가세 별도 · 현장 진단 후 선견적 제공</caption>
      <thead><tr><th scope="col">서비스 항목</th><th scope="col">작업 범위</th><th scope="col">예상 요금</th></tr></thead>
      <tbody>
        <tr><td>하수구막힘</td><td>일반 관로 뚫음 (스프링/관통)</td><td class="unit">5만원~</td></tr>
        <tr><td>변기·싱크대막힘</td><td>이물질 제거·압력 관통</td><td class="unit">4만원~</td></tr>
        <tr><td>바닥 배수구</td><td>이물질 제거</td><td class="unit">4만원~</td></tr>
        <tr><td>고압세척</td><td>관 내부 기름때·스케일 세척 (m당)</td><td class="unit">별도 산정</td></tr>
        <tr><td>누수탐지</td><td>비파괴 정밀 탐지 (지점당)</td><td class="unit">10만원~</td></tr>
        <tr><td>CCTV 관로검사</td><td>관 내부 영상 진단</td><td class="unit">8만원~</td></tr>
        <tr><td>배관공사</td><td>노후관 교체·신설</td><td class="unit">현장 견적</td></tr>
        <tr><td>정화조 관리</td><td>청소·준설</td><td class="unit">현장 견적</td></tr>
        <tr><td>동파 복구</td><td>해빙·보수</td><td class="unit">현장 견적</td></tr>
      </tbody>
    </table></div>

    <h2>요금이 달라지는 요인</h2>
    <ul class="ticks">
      <li>막힘·누수의 위치와 정도, 관의 길이·관경</li>
      <li>현장 접근성(층수·매립 여부·작업 공간)</li>
      <li>야간·휴일 긴급 출동 여부</li>
      <li>사용 자재의 등급과 보증 범위</li>
    </ul>

    <h2>상업시설 정기 관리 계약</h2>
    <p>호텔·식당·빌딩 등 주기적 관리가 필요한 시설은 월/분기 단위 정기 관리 계약으로 <strong>우선 출동과 요금 할인</strong>을 받을 수 있습니다. 세금계산서·거래명세서 발행을 지원합니다.</p>
    <p style="margin-top:24px;"><a class="btn btn--primary" href="/contact.html">정확한 견적 무료 상담</a></p>
  </div>
</section>
{bottom_cta()}
</main>
"""
page("price.html","요금안내 | 하수구막힘·누수탐지·고압세척 예상 요금 - 스피드 배관공사",
     "스피드 배관공사 요금안내. 하수구막힘, 누수탐지, 고압세척, 배관공사 등 상업시설 배관 서비스의 참고 단가와 정기 관리 계약 안내. 선견적 후작업, 추가금 없음.",
     S + "/price.html", price_body, jsonld=breadcrumb_jsonld([("홈","/"),("요금안내","/price.html")]))

# ===========================================================================
# 고객후기
# ===========================================================================
REV = [
    (5,"야간에 호텔 객실 층 배수가 막혔는데 30분 만에 오셔서 영업에 지장 없이 해결해주셨어요. 견적도 먼저 정확히 알려주셔서 믿음이 갔습니다.","김","김OO 지배인","서울 강남 · 호텔"),
    (5,"상가 화장실 누수 원인을 다른 곳에선 못 찾았는데, 벽 안 뜯고 정확히 짚어주셔서 복구비를 크게 아꼈습니다. 세금계산서도 깔끔하게 처리됐어요.","이","이OO 점주","경기 성남 · 상가"),
    (5,"빌딩 지하 배관 교체를 야간 무중단으로 진행해 주셔서 입주사 불만 없이 끝냈습니다. 정기 관리까지 맡기기로 했어요.","박","박OO 관리소장","부산 해운대 · 오피스빌딩"),
    (5,"주방 배관이 자주 막혀 골치였는데 고압세척 후로 확실히 좋아졌습니다. 정기 세척 주기도 잡아주셔서 편해요.","최","최OO 대표","서울 마포 · 식당"),
    (5,"CCTV로 막힘 원인을 직접 보여주시니 신뢰가 갔습니다. 불필요한 공사 없이 필요한 부분만 정확히.","정","정OO 실장","인천 · 상가"),
    (4,"주말 새벽에 변기 막힘으로 급하게 연락드렸는데 빠르게 와주셨어요. 응대도 친절했습니다.","한","한OO 사장","수원 · 숙박"),
]
rcards = ""
for star, txt, av, who, where in REV:
    stars = "★"*star + "☆"*(5-star)
    rcards += f"""<article class="review-card"><div class="stars" aria-label="별점 {star}점">{stars}</div><blockquote>“{txt}”</blockquote><div class="review-meta"><span class="review-avatar">{av}</span><div><div class="who">{who}</div><div class="where">{where}</div></div></div></article>"""
review_body = f"""{phero("Reviews","고객후기","실제 고객이 남긴 후기입니다. 더 많은 후기는 네이버 플레이스에서 확인하실 수 있습니다.",[("홈","/"),("고객후기",None)])}
<main>
<section class="section">
  <div class="container">
    <div class="review-grid">{rcards}</div>
    <p style="text-align:center;margin-top:36px;"><a class="btn btn--primary" href="https://map.naver.com/" rel="noopener" target="_blank">네이버 플레이스에서 더 보기</a></p>
  </div>
</section>
{bottom_cta()}
</main>
"""
page("review.html","고객후기 | 상업시설 배관 서비스 후기 - 스피드 배관공사",
     "스피드 배관공사 고객후기. 호텔·상가·빌딩 고객이 직접 남긴 하수구막힘, 누수탐지, 고압세척 서비스 후기를 확인하세요. 누적 평점 4.9.",
     S + "/review.html", review_body, jsonld=breadcrumb_jsonld([("홈","/"),("고객후기","/review.html")]))

# ===========================================================================
# FAQ
# ===========================================================================
FAQ_FULL = FAQ_ITEMS + [
    ("출장비나 점검비가 따로 있나요?","현장 진단 후 작업을 진행하는 경우 별도 출장비를 청구하지 않는 것이 원칙입니다. 단순 점검·진단만 진행되는 경우의 비용은 사전에 안내드립니다."),
    ("정기 관리 계약은 어떻게 진행되나요?","시설 규모와 사용량을 진단해 월/분기 단위 관리 주기와 요금을 제안합니다. 계약 시 우선 출동과 요금 할인이 적용됩니다."),
    ("작업 후 문제가 재발하면 어떻게 하나요?","작업 항목별 사후 보증을 적용합니다. 동일 원인으로 재발 시 보증 범위 내에서 재작업해 드리며, 보증 조건은 작업 전 안내합니다."),
]
faq_page_body = f"""{phero("FAQ","자주묻는질문","상담 전 자주 궁금해하시는 내용을 모았습니다. 더 궁금한 점은 언제든 전화로 문의해 주세요.",[("홈","/"),("자주묻는질문",None)])}
<main>
<section class="section">
  <div class="container">
    <div class="faq-list">
{faq_html(FAQ_FULL)}    </div>
  </div>
</section>
{bottom_cta()}
</main>
"""
page("faq.html","자주묻는질문 | 상업시설 배관 서비스 FAQ - 스피드 배관공사",
     "스피드 배관공사 자주 묻는 질문. 24시간 출동, 선견적 후작업, 누수탐지 방식, 세금계산서 발행, 정기 관리 계약 등 상업시설 배관 서비스 관련 궁금증을 확인하세요.",
     S + "/faq.html", faq_page_body, jsonld=breadcrumb_jsonld([("홈","/"),("자주묻는질문","/faq.html")]) + faq_jsonld(FAQ_FULL))

# ===========================================================================
# 회사소개
# ===========================================================================
about_body = f"""{phero("About","회사소개","상업시설 배관, 멈추지 않는 신속함. 스피드 배관공사는 호텔·상가·오피스빌딩의 배관을 책임지는 B2B 전문 파트너입니다.",[("홈","/"),("회사소개",None)])}
<main>
<section class="section">
  <div class="container prose" style="max-width:880px;">
    <h2>우리가 일하는 방식</h2>
    <p>스피드 배관공사는 ‘영업을 멈추지 않게 한다’는 한 가지 원칙에서 출발합니다. 호텔의 객실, 식당의 주방, 빌딩의 지하 배관은 한 번 멈추면 곧 매출 손실로 이어집니다. 그래서 우리는 <strong>빠른 출동</strong>과 <strong>정직한 견적</strong>, 그리고 <strong>재발을 막는 근본 처리</strong>를 기준으로 일합니다.</p>

    <h2>우리의 약속</h2>
    <ul class="ticks">
      <li><strong>24시간 출동</strong> — 야간·휴일에도 가까운 작업팀이 즉시 움직입니다.</li>
      <li><strong>선견적 후작업</strong> — 비용을 먼저 안내하고, 동의 후에만 작업합니다.</li>
      <li><strong>상업시설 전문</strong> — 대형 배관·설비에 맞는 인력과 장비를 갖췄습니다.</li>
      <li><strong>투명한 거래</strong> — 세금계산서·현금영수증 발행, 정기 관리 계약 지원.</li>
    </ul>

    <h2>전문 장비</h2>
    <div class="chips"><span>고압세척기(워터젯)</span><span>CCTV 관로카메라</span><span>청음식 누수탐지기</span><span>열화상 카메라</span><span>전동 스프링·관통기</span><span>전기 융착기</span><span>가압 테스트 펌프</span></div>

    <h2>회사 정보</h2>
    <div class="price-table-wrap"><table class="price-table">
      <tbody>
        <tr><td>상호</td><td colspan="2">스피드 배관공사 (SPEED PLUMBING)</td></tr>
        <tr><td>대표자</td><td colspan="2">(미정)</td></tr>
        <tr><td>사업자등록번호</td><td colspan="2">000-00-00000</td></tr>
        <tr><td>주소</td><td colspan="2">(미정)</td></tr>
        <tr><td>대표전화</td><td colspan="2">1577-0000</td></tr>
        <tr><td>카카오톡</td><td colspan="2">@스피드배관</td></tr>
        <tr><td>영업시간</td><td colspan="2">연중무휴 24시간</td></tr>
      </tbody>
    </table></div>
  </div>
</section>
{bottom_cta()}
</main>
"""
page("about.html","회사소개 | 상업시설 전문 B2B 배관 파트너 - 스피드 배관공사",
     "스피드 배관공사 회사소개. 호텔·상가·오피스빌딩 배관을 책임지는 상업시설 전문 B2B 파트너. 24시간 출동, 선견적 후작업, 전문 장비와 투명한 거래를 약속합니다.",
     S + "/about.html", about_body, jsonld=breadcrumb_jsonld([("홈","/"),("회사소개","/about.html")]))

# ===========================================================================
# 상담문의
# ===========================================================================
contact_body = f"""{phero("Contact","상담문의","전화 한 통이면 가장 가까운 전문 작업팀이 움직입니다. 24시간 언제든 연락 주시고, 견적 폼으로도 신청하실 수 있습니다.",[("홈","/"),("상담문의",None)])}
<main>
<section class="section">
  <div class="container layout-sidebar">
    <div>
      <h2>무료 견적 신청</h2>
      <p class="lead" style="margin-bottom:24px;">아래 정보를 남겨주시면 빠르게 연락드려 현장 진단·견적을 안내해 드립니다.</p>
      <form data-quote-form novalidate>
        <div class="form-grid">
          <div class="field"><label for="name">이름/담당자 <span class="req">*</span></label><input id="name" name="name" type="text" required autocomplete="name"></div>
          <div class="field"><label for="phone">연락처 <span class="req">*</span></label><input id="phone" name="phone" type="tel" required autocomplete="tel" placeholder="010-0000-0000"></div>
          <div class="field"><label for="facility">시설 유형</label>
            <select id="facility" name="facility">
              <option value="">선택</option><option>호텔·숙박</option><option>상가·식당</option><option>오피스빌딩</option><option>공장·물류</option><option>기타</option>
            </select>
          </div>
          <div class="field"><label for="service">필요 서비스</label>
            <select id="service" name="service">
              <option value="">선택</option><option>하수구막힘</option><option>배관공사</option><option>누수탐지</option><option>고압세척</option><option>CCTV 관로검사</option><option>기타</option>
            </select>
          </div>
          <div class="field full"><label for="region">지역</label><input id="region" name="region" type="text" placeholder="예) 서울 강남구"></div>
          <div class="field full"><label for="msg">증상/요청 내용</label><textarea id="msg" name="msg" placeholder="증상과 현장 상황을 적어주시면 더 정확히 안내해 드립니다."></textarea></div>
          <div class="field full">
            <label class="form-consent"><input type="checkbox" name="consent" required style="margin-top:4px;"> <span>개인정보 수집·이용에 동의합니다. (상담 목적, 보관 후 파기)</span></label>
          </div>
          <div class="field full">
            <button class="btn btn--primary btn--lg" type="submit">상담 신청하기</button>
            <p class="form-status price-note" role="status" hidden></p>
          </div>
        </div>
      </form>
    </div>
    <aside class="sidebar-card">
      <h3>바로 연락하기</h3>
      <p>24시간 상업시설 전문 출동. 급하실 땐 전화가 가장 빠릅니다.</p>
      <a class="phone-big" href="tel:1577-0000">1577-0000</a>
      <ul class="info-list" style="margin-top:18px;color:#BFD0E8;list-style:none;">
        <li style="display:block;color:#BFD0E8;">카카오톡 상담: <strong style="color:#fff;">@스피드배관</strong></li>
        <li style="display:block;color:#BFD0E8;">영업시간: <strong style="color:#fff;">연중무휴 24시간</strong></li>
      </ul>
      <a class="btn btn--primary btn--block" href="tel:1577-0000" style="margin-top:16px;">☎ 전화 상담</a>
      <a class="btn btn--ghost-light btn--block" href="https://pf.kakao.com/" target="_blank" rel="noopener" style="margin-top:10px;">카카오톡 상담</a>
    </aside>
  </div>
</section>
</main>
"""
page("contact.html","상담문의 | 무료 견적·24시간 출동 - 스피드 배관공사",
     "스피드 배관공사 상담문의. 전화 1577-0000 또는 무료 견적 폼으로 신청하세요. 호텔·상가·빌딩 배관 24시간 상업시설 전문 출동, 선견적 후작업.",
     S + "/contact.html", contact_body, jsonld=breadcrumb_jsonld([("홈","/"),("상담문의","/contact.html")]))

# ===========================================================================
# 404
# ===========================================================================
notfound_body = """<main>
<section class="section" style="text-align:center;min-height:50vh;display:grid;place-items:center;">
  <div class="container" style="max-width:560px;">
    <span class="eyebrow">404</span>
    <h1>페이지를 찾을 수 없습니다</h1>
    <p class="lead">요청하신 페이지가 이동되었거나 존재하지 않습니다. 아래에서 원하시는 정보를 찾아보세요.</p>
    <p style="margin-top:24px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
      <a class="btn btn--primary" href="/">홈으로</a>
      <a class="btn btn--secondary" href="/service/">서비스안내</a>
      <a class="btn btn--secondary" href="/contact.html">상담문의</a>
    </p>
  </div>
</section>
</main>
"""
page("404.html","페이지를 찾을 수 없습니다 (404) - 스피드 배관공사",
     "요청하신 페이지를 찾을 수 없습니다. 스피드 배관공사 홈으로 이동하거나 서비스안내·상담문의를 이용해 주세요.",
     S + "/404.html", notfound_body)

print("\\nALL PAGES BUILT.")


# ===========================================================================
# 시도 추가 확장 (각 시도 고유 콘텐츠 — 도어웨이 방지)
# ===========================================================================
def _case(tag, title, desc, b, a, alt_b, alt_a):
    return (f"""<article class="case-card" style="max-width:520px;"><div class="ba">"""
            f"""<figure class="before"><img src="/assets/img/{b}" alt="{alt_b}" loading="lazy" width="400" height="300"><figcaption>BEFORE</figcaption></figure>"""
            f"""<figure class="after"><img src="/assets/img/{a}" alt="{alt_a}" loading="lazy" width="400" height="300"><figcaption>AFTER</figcaption></figure></div>"""
            f"""<div class="case-body"><span class="case-tag">{tag}</span><h3>{title}</h3><p>{desc}</p></div></article>""")

# (slug, name, short, intro, districts, case, phone_note)
SIDO_MORE = [
 ("daegu","대구광역시",
  "동성로·서문시장 등 도심 상권과 산업단지가 함께 있는 대구는 식당가 주방 배관과 공장 오수관 관리 수요가 꾸준합니다. 도심·외곽 권역에 작업팀을 배치해 빠르게 대응합니다.",
  "여름철 무더위로 음식물 부패가 빠른 대구 식당가 특성상 기름때 하수구막힘 의뢰가 많고, 노후 상가 건물의 배관 교체도 자주 진행합니다. 고압세척과 CCTV 진단으로 재발까지 관리합니다.",
  ["중구","동구","서구","남구","북구","수성구","달서구","달성군"],
  _case("중구 · 식당가","동성로 식당 주방 배관 고압세척","여름철 반복되던 기름때 막힘을 고압세척으로 해소.","case1.svg","case1-after.svg","대구 중구 식당 주방 배관 막힘 전","대구 중구 식당 주방 고압세척 후"),
  "대구 도심·외곽 24시간 출동."),
 ("incheon","인천광역시",
  "공항·항만·물류단지와 신도시 상가가 공존하는 인천은 대형 시설의 배관 규모가 크고, 송도·청라 신도시 상가의 신축 배관 수요도 많습니다. 권역별 작업팀으로 폭넓게 대응합니다.",
  "물류·공장 시설의 대형 오수관 고압세척과, 송도·청라 상가의 주방 배관 막힘을 함께 처리합니다. 해안 매립지 특성상 배관 침하·역구배 점검도 CCTV로 진단합니다.",
  ["중구","미추홀구","연수구","남동구","부평구","계양구","서구","강화군"],
  _case("연수구 · 상가","송도 상가 배관 CCTV 진단","반복 막힘 원인을 영상으로 특정해 정확히 보수.","case2.svg","case2-after.svg","인천 연수구 상가 배관 진단 전","인천 연수구 상가 배관 보수 후"),
  "인천 전역·도서 권역 24시간 출동."),
 ("gwangju","광주광역시",
  "충장로·상무지구 등 상업 중심지와 첨단산단을 갖춘 광주는 식당·카페 상권의 배관 관리와 사무빌딩 배관 수요가 많습니다. 시 전역에 작업팀을 운영합니다.",
  "상무지구 오피스빌딩의 누수탐지·배관 교체와, 충장로 상권 식당의 하수구막힘을 함께 대응합니다. 선견적 후작업으로 비용을 먼저 확인하고 진행합니다.",
  ["동구","서구","남구","북구","광산구"],
  _case("서구 · 빌딩","상무지구 빌딩 지하 누수탐지","벽 철거 없이 누수 지점을 특정해 복구비 절감.","case2.svg","case2-after.svg","광주 서구 빌딩 누수 전","광주 서구 빌딩 누수 보수 후"),
  "광주 전역 24시간 출동."),
 ("daejeon","대전광역시",
  "둔산·유성 등 업무·연구단지와 원도심 상권이 어우러진 대전은 연구시설·사무빌딩의 배관과 식당가 배관 관리 수요가 함께 있습니다. 도심·유성 권역에 작업팀을 배치합니다.",
  "둔산 오피스빌딩의 노후관 교체와 유성 상권 주방 배관 고압세척을 주로 진행합니다. 정기 관리 계약으로 우선 출동·요금 할인을 제공합니다.",
  ["동구","중구","서구","유성구","대덕구"],
  _case("서구 · 오피스","둔산 오피스 노후관 교체","부식 메인 배관을 야간 무중단으로 교체.","case3.svg","case3-after.svg","대전 서구 오피스 배관 노후 전","대전 서구 오피스 배관 교체 후"),
  "대전 도심·유성 권역 24시간 출동."),
 ("ulsan","울산광역시",
  "산업수도 울산은 대규모 공장·플랜트 설비 배관과 상권 식당 배관이 공존합니다. 산업단지 대형 배관에 맞는 장비와 인력으로 대응합니다.",
  "공장·플랜트 오수관 고압세척과 CCTV 진단, 상가 식당의 하수구막힘을 함께 처리합니다. 대형 관로 작업 경험을 갖춘 팀이 출동합니다.",
  ["중구","남구","동구","북구","울주군"],
  _case("남구 · 산업시설","산업단지 오수관 고압세척","대형 관로 슬러지를 제거해 배수 정상화.","case1.svg","case1-after.svg","울산 남구 산업시설 오수관 전","울산 남구 산업시설 오수관 세척 후"),
  "울산 산업단지·도심 24시간 출동."),
 ("sejong","세종특별자치시",
  "행정중심복합도시로 빠르게 성장한 세종은 신축 상가·오피스가 밀집해 신규 배관과 초기 하자 점검 수요가 많습니다. 신도심 전역으로 신속 출동합니다.",
  "신축 상가의 배관 마감·하자 점검과 식당 주방 배관 막힘을 주로 대응합니다. CCTV 진단으로 시공 상태를 영상으로 확인해 드립니다.",
  ["한솔동","도담동","아름동","종촌동","새롬동","보람동","조치원읍"],
  _case("신도심 · 상가","세종 상가 배관 CCTV 점검","신축 배관 상태를 영상으로 확인 후 보수.","case2.svg","case2-after.svg","세종 상가 배관 점검 전","세종 상가 배관 보수 후"),
  "세종 신도심 전역 24시간 출동."),
 ("gangwon","강원특별자치도",
  "관광·숙박 시설이 많은 강원은 성수기 호텔·콘도·펜션의 배관 긴급 대응과 겨울철 동파 복구 수요가 특히 높습니다. 영동·영서 권역에 작업팀을 운영합니다.",
  "성수기 숙박시설 객실 배수 긴급 대응과 겨울철 동파 해빙·복구를 집중적으로 진행합니다. 한랭지 배관 보온·보수 경험을 갖춘 팀이 출동합니다.",
  ["춘천시","원주시","강릉시","속초시","동해시","삼척시","평창군","홍천군"],
  _case("강릉 · 숙박","강릉 펜션 객실 동파 복구","겨울철 동파관을 해빙·보수해 영업 재개.","case3.svg","case3-after.svg","강원 강릉 펜션 동파 전","강원 강릉 펜션 동파 복구 후"),
  "강원 영동·영서 권역 24시간 출동, 동파 전문."),
 ("chungbuk","충청북도",
  "청주를 중심으로 산업단지와 물류시설이 발달한 충북은 공장 오수관 관리와 상권 식당 배관 수요가 함께 있습니다. 청주·충주 권역에 작업팀을 배치합니다.",
  "청주 산업단지의 대형 오수관 고압세척과 상가 식당의 하수구막힘을 주로 처리합니다. 정기 관리로 막힘 빈도를 크게 줄입니다.",
  ["청주시","충주시","제천시","음성군","진천군","옥천군","영동군"],
  _case("청주 · 식당","청주 식당가 주방 배관 세척","기름때 누적 배관을 고압세척으로 회복.","case1.svg","case1-after.svg","충북 청주 식당 배관 전","충북 청주 식당 배관 세척 후"),
  "충북 청주·충주 권역 24시간 출동."),
 ("chungnam","충청남도",
  "천안·아산 산업벨트와 서해안 관광지를 아우르는 충남은 공장·물류 배관과 숙박시설 배관 수요가 함께 있습니다. 내륙·서해안 권역에 작업팀을 운영합니다.",
  "천안·아산 물류시설의 대형 배관 고압세척과 서해안 숙박시설의 객실 배수 긴급 대응을 함께 진행합니다. CCTV 진단으로 근본 원인을 찾습니다.",
  ["천안시","아산시","서산시","당진시","공주시","논산시","보령시","예산군"],
  _case("천안 · 물류","천안 물류센터 오수관 세척","대형 관로 슬러지 제거로 배수 정상화.","case1.svg","case1-after.svg","충남 천안 물류센터 오수관 전","충남 천안 물류센터 오수관 세척 후"),
  "충남 내륙·서해안 권역 24시간 출동."),
 ("jeonbuk","전북특별자치도",
  "전주 한옥마을 상권과 군산·익산 산업지역을 갖춘 전북은 관광 식당가 배관과 공장 배관 수요가 함께 있습니다. 전주·군산 권역에 작업팀을 배치합니다.",
  "전주 상권 식당의 기름때 하수구막힘과 군산·익산 공장의 오수관 관리를 주로 대응합니다. 선견적 후작업으로 신뢰를 드립니다.",
  ["전주시","군산시","익산시","정읍시","남원시","김제시","완주군"],
  _case("전주 · 식당가","전주 식당가 배관 고압세척","관광 성수기 전 배관을 미리 세척해 막힘 예방.","case1.svg","case1-after.svg","전북 전주 식당가 배관 전","전북 전주 식당가 배관 세척 후"),
  "전북 전주·군산 권역 24시간 출동."),
 ("jeonnam","전라남도",
  "여수·순천·목포 등 관광·항만 도시가 많은 전남은 숙박·식당 시설의 배관과 항만 시설 배관 수요가 함께 있습니다. 동부·서부 권역에 작업팀을 운영합니다.",
  "여수·순천 숙박시설의 객실 배수 긴급 대응과 목포 상권 식당의 배관 막힘을 함께 처리합니다. 해안 노후 배관의 부식·누수도 점검합니다.",
  ["목포시","여수시","순천시","나주시","광양시","무안군","해남군","고흥군"],
  _case("여수 · 숙박","여수 호텔 객실 배수 긴급 대응","성수기 야간 막힘을 신속 출동으로 해결.","case3.svg","case3-after.svg","전남 여수 호텔 배수 전","전남 여수 호텔 배수 복구 후"),
  "전남 동부·서부 권역 24시간 출동."),
 ("gyeongbuk","경상북도",
  "포항·구미 산업도시와 경주 관광지를 아우르는 경북은 공장 대형 배관과 숙박시설 배관 수요가 함께 있습니다. 포항·구미·경주 권역에 작업팀을 배치합니다.",
  "포항·구미 산업단지의 오수관 고압세척·CCTV 진단과 경주 숙박시설의 배관 관리를 함께 진행합니다. 대형 관로 작업 경험을 갖춘 팀이 출동합니다.",
  ["포항시","구미시","경주시","경산시","안동시","김천시","영주시","칠곡군"],
  _case("구미 · 산업시설","구미 산단 오수관 CCTV 진단","관 내부 파손을 영상으로 확인 후 보수.","case2.svg","case2-after.svg","경북 구미 산단 오수관 진단 전","경북 구미 산단 오수관 보수 후"),
  "경북 포항·구미·경주 권역 24시간 출동."),
 ("gyeongnam","경상남도",
  "창원·김해 산업벨트와 통영·거제 해안 관광지를 갖춘 경남은 공장 배관과 숙박·식당 배관 수요가 함께 있습니다. 동부·서부 권역에 작업팀을 운영합니다.",
  "창원·김해 공장의 대형 오수관 관리와 통영·거제 숙박시설의 객실 배수 대응을 함께 진행합니다. 해안 노후 배관의 부식·누수도 정밀 탐지합니다.",
  ["창원시","김해시","진주시","양산시","거제시","통영시","사천시","밀양시"],
  _case("창원 · 공장","창원 공장 오수관 고압세척","대형 관로 슬러지 제거로 배수 회복.","case1.svg","case1-after.svg","경남 창원 공장 오수관 전","경남 창원 공장 오수관 세척 후"),
  "경남 동부·서부 권역 24시간 출동."),
 ("jeju","제주특별자치도",
  "관광·숙박 산업이 중심인 제주는 호텔·리조트·게스트하우스의 배관 긴급 대응 수요가 특히 높습니다. 제주시·서귀포 권역에 작업팀을 운영합니다.",
  "성수기 숙박시설의 객실 배수 긴급 대응과 식당가 주방 배관 고압세척을 집중적으로 진행합니다. 화산암 지반 특성을 고려한 배관 점검도 함께합니다.",
  ["제주시","서귀포시","애월읍","조천읍","한림읍","성산읍","대정읍","남원읍"],
  _case("제주시 · 숙박","제주 리조트 객실 배수 대응","성수기 야간 막힘을 신속 출동으로 해결.","case3.svg","case3-after.svg","제주시 리조트 배수 전","제주시 리조트 배수 복구 후"),
  "제주시·서귀포 권역 24시간 출동."),
]
for slug, name, short, intro, districts, case, note in SIDO_MORE:
    sido_page(slug, name, short, intro, districts, {}, case, note)

print("\\nEXTRA SIDO PAGES BUILT.")
