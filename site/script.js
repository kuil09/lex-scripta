const revealElements = document.querySelectorAll(".reveal");

window.setTimeout(() => {
  revealElements.forEach((element) => element.classList.add("is-visible"));
}, 220);

revealElements.forEach((element, index) => {
  element.style.setProperty("--delay", `${Math.min(index * 40, 200)}ms`);
});

if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      });
    },
    {
      threshold: 0.14,
    }
  );

  revealElements.forEach((element) => revealObserver.observe(element));
} else {
  revealElements.forEach((element) => element.classList.add("is-visible"));
}

document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const command = button.getAttribute("data-copy");
    const defaultText = button.getAttribute("data-copy-default") || "Copy command";
    const successText = button.getAttribute("data-copy-success") || "Copied";
    const failureText = button.getAttribute("data-copy-failure") || "Copy failed";

    if (!command) {
      return;
    }

    try {
      await navigator.clipboard.writeText(command);
      button.textContent = successText;
      button.classList.add("is-copied");

      window.setTimeout(() => {
        button.textContent = defaultText;
        button.classList.remove("is-copied");
      }, 1400);
    } catch (error) {
      button.textContent = failureText;

      window.setTimeout(() => {
        button.textContent = defaultText;
      }, 1400);
    }
  });
});
