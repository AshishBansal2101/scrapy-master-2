document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("div.highlight pre").forEach((block) => {
    // Create copy button
    const button = document.createElement("button");
    button.innerText = "📋 Copy";
    button.className = "copy-btn";
    block.parentNode.style.position = "relative";
    block.parentNode.appendChild(button);

    // On click, copy text
    button.addEventListener("click", async () => {
      const code = block.innerText;
      await navigator.clipboard.writeText(code);
      button.innerText = "✅ Copied!";
      setTimeout(() => (button.innerText = "📋 Copy"), 1500);
    });
  });
});
