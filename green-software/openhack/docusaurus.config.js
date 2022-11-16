// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

const organizationName = 'azure';
const repoName = "sustainaiblity"
const projectName = "green-software";

/** @type {import('@docusaurus/types').Config} */
const config = {

  title: "Build green software applications on Azure",
  tagline: "Learn how to build applications on Azure with sustainability in mind",
  url: `https://${organizationName}.github.io`,
  baseUrl: `/${repoName}/${projectName}/`,
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "throw",
  favicon: "./static/img/favicon.ico",

  // GitHub Pages adds a trailing slash by default that I don't want
  trailingSlash: false,

  organizationName,
  repoName,
  projectName,
  
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: DataTransferItemList,
        logo: {
          alt: "Build green software applications on Azure",
          src: "./static/img/logo.svg",
        },
        items: [
          {
          position: 'left',
          type: "doc",
          docId: "intro",
          label: 'Resources',
          },
          {
            href: `https://github.com/${organizationName}/${repoName}/${projectName}`,
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "Resources",
                to: "./docs/intro",
              },
            ],
          },
          {
            title: "Community",
            items: [
              {
                label: "Stack Overflow",
                href: "https://stackoverflow.com/questions/tagged/docusaurus",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "GitHub",
                href: `https://github.com/${organizationName}/${repoName}/${projectName}`,
              },
            ],
          },
        ],
        copyright: `by Microsoft Open Source community.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
