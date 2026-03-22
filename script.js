const featuredProjects = [
  {
    badge: "robot sim",
    title: "Autonomous Shopper Assistance System",
    description:
      "A simulated robot that navigates autonomously to the desired item in a supermarket.",
    meta: ["ROS2", "LangChain", "MongoDB", "Fast API", "Python", "ReactJS"],
    links: [
      {
        label: "Source",
        href: "https://github.com/muditmehta07/asas",
      },
    ],
  },
  {
    badge: "ai-agent",
    title: "Software Installation Agent",
    description:
      "An AI-agent that recommends relevant proprietary applications enabling on-the-go access to matched tools.",
    meta: ["LangChain", "Azure Vector Database", "OpenAI", "Python"],
    links: [
      {
        label: "Source",
        href: "https://github.com/muditmehta07/software-installation-agent",
      },
    ],
  }
];

const projectGrid = document.getElementById("project-grid");
const year = document.getElementById("year");

featuredProjects.forEach((project) => {
  const card = document.createElement("article");
  card.className = "project-card";

  const metaMarkup = project.meta.map((item) => `<span>${item}</span>`).join("");
  const linksMarkup = project.links
    .map(
      (link) =>
        `<a href="${link.href}" target="_blank" rel="noreferrer">${link.label}</a>`
    )
    .join("");

  card.innerHTML = `
    <span class="project-badge">${project.badge}</span>
    <h3 class="project-title">${project.title}</h3>
    <p>${project.description}</p>
    <div class="project-meta">${metaMarkup}</div>
    <div class="project-links">${linksMarkup}</div>
  `;

  projectGrid.appendChild(card);
});

year.textContent = new Date().getFullYear().toString();

lucide.createIcons();