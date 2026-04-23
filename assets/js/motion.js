// Subtle, one-shot reveal motion. Respects prefers-reduced-motion.
(function () {
  "use strict";

  var reduce =
    window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var hero = document.querySelector(".hero");
  var reveals = document.querySelectorAll(".reveal");

  if (reduce) {
    if (hero) hero.classList.add("is-visible");
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }

  // Hero: play the staggered load animation on next frame.
  if (hero) {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        hero.classList.add("is-visible");
      });
    });
  }

  // Sections: reveal once as they scroll into view.
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }
})();
