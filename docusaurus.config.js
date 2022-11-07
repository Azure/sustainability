// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");

/** @type {import('@docusaurus/types').Config} */
const config = {
  // Change to Site title
  title: "Learn Green Software on Azure",
  // Change to site description
  tagline: "Learn how to make your Azure solutions more sustainable and carbon aware",
  // Change to site url
  url: "https://azure.github.io",
  baseUrl: "/sustainability/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "Microsoft",
  // Change to GitHub repo name.
  projectName: "sustainability",
  deploymentBranch: "gh-pages",
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
          routeBasePath: "/",
          // Change this to your repo.
          editUrl: "https://github.com/Azure/sustainability/tree/main/",
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
        gtag: {
          trackingID: "Gqsdsd",
        },
        sitemap: {
          changefreq: "weekly",
          priority: 0.5,
          ignorePatterns: ["/tags/**"],
          filename: "sitemap.xml",
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        // Change to project name
        title: "Green Software on Azure",
        logo: {
          alt: "Green Software Logo",
          src: "img/logo.svg",
        },
      },
      footer: {
        style: "dark",
        links: [{
          title: "Links",
          items: [{
            label: "Github",
            href: "https://github.com/Azure/sustainability",
          },
          ],
        },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Microsoft Open Source.`,
      },
      prism: {
        theme: lightCodeTheme,
      },
      colorMode: {
        disableSwitch: true,
        defaultMode: "dark",
      },
    }),
  plugins: [
    [
      "@docusaurus/plugin-ideal-image",
      {
        quality: 90,
        max: 1030, // max resized image's size.
        min: 640, // min resized image's size. if original is lower, use that size.
        steps: 2, // the max number of images generated between min and max (inclusive)
        disableInDev: false,
      },
    ],
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [ // The course was originally posted under practitioner
          {
            to: '/introduction',
            from: '/practitioner/introduction',
          },
         
        ]
      },
    ],
  ],
};

module.exports = config;
