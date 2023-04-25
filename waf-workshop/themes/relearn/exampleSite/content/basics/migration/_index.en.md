+++
disableToc = false
title = "What's New"
weight = 2
+++

This document shows you what's new in the latest release. For a detailed list of changes, see the [history page]({{%relref "basics/history" %}}).

{{% badge color="fuchsia" icon="fab fa-hackerrank" title=" " %}}0.95.0{{% /badge %}} The minimum required Hugo version.

{{% badge style="warning" title=" " %}}Breaking{{% /badge %}} A change that requires action by you after upgrading to assure the site is still functional.

{{% badge style="note" title=" " %}}Change{{% /badge %}} A change in default behavior that may requires action by you if you want to revert it.

{{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Marks new behavior you might find interesting or comes configurable.

<!--GH-ACTION-RELEASE-MILESTONE-->

---

## 5.12.0 (2023-03-28)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} In the effort to comply with WCAG standards, the implementation of the collapsible menu was changed (again). While Internet Explorer 11 has issues in displaying it, the functionality still works.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Support for the great [VSCode Front Matter extension](https://github.com/estruyf/vscode-front-matter) which provides on-premise CMS capabilties to Hugo.

  The theme provides Front Matter snippets for its shortcodes. Currently only English and German is supported. Put a reference into your `frontmatter.json` like this

  ````json
  {
    ...
    "frontMatter.extends": [
        "./vscode-frontmatter/snippets.en.json"
    ]
    ...
  }
  ````

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Support for languages that are written right to left (like Arabic) is now complete and extended to the menu, the top navigation bar and print. You can experience this in the [pirate translation]({{%relref path="basics/migration" lang="pir" %}}). This feature is not available in Internet Explorer 11.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The scrollbars are now colored according to their variant color scheme to better fit into the visuals.

---

## 5.11.0 (2023-02-07)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The theme removed the popular [jQuery](https://jquery.com) library from its distribution.

  In case you made changes to the theme that are dependend on this library you can place a copy of jQuery into your `static/js` directory and load it from your own `layouts/partials/custom-header.html` like this:

  ````html
  <script src="{{"js/jquery.min.js"| relURL}}" defer></script>
  ````

- {{% badge style="note" title=" " %}}Change{{% /badge %}} [Mermaid]({{% relref "shortcodes/mermaid#parameter" %}}) diagrams can now be configured for pan and zoom on site-, page-level or individually for each graph.

  The default setting of `on`, in effect since 1.1.0, changed back to `off` as there was interference with scrolling on mobile and big pages.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The theme is now capable to visually [adapt to your OS's light/dark mode setting]({{%relref "basics/customization/#adjust-to-os-settings" %}}).

  This is also the new default setting if you haven't configured `themeVariant` in your `config.toml`.

  Additionally you can configure the variants to be taken for light/dark mode with the new `themeVariantAuto` parameter.

  This is not supported for Internet Explorer 11, which still displays in the `relearn-light` variant.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The JavaScript code for handling image lightboxes (provided by [Featherlight](https://noelboss.github.io/featherlight)) was replaced by a CSS-only solution.

  This also changed the [lightbox effects]({{% relref "cont/markdown#lightbox" %}}) parameter from `featherlight=false` to `lightbox=false`. Nevertheless you don't need to change anything as the old name will be used as a fallback.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} In the effort to comply with WCAG standards, the implementation of the [`expand` shortcode]({{% relref "shortcodes/expand" %}}) was changed. While Internet Explorer 11 has issues in displaying it, the functionality still works.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Translation for Czech. This language is not supported for search.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} [GitHub releases](https://github.com/McShelby/hugo-theme-relearn/tags) are also now tagged for the main version (eg. `1.2.x`), major version (eg. `1.x`) and the latest (just `x`) release making it easier for you to pin the theme to a certain version.

---

## 5.10.0 (2023-01-25)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The [`attachments`]({{% relref "shortcodes/attachments" %}}), [`badge`]({{% relref "shortcodes/badge" %}}), [`button`]({{% relref "shortcodes/button" %}}) and [`notice`]({{% relref "shortcodes/notice" %}}) shortcodes have a new parameter `color` to set arbitrary CSS color values.

  Additionally the `--ACCENT-color` brand color introduced in version 5.8.0 is now supported with these shortcodes.

---

## 5.9.0 (2022-12-23)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The required folder name for the [`attachments` shortcode]({{% relref "shortcodes/attachments" %}}) was changed for leaf bundles.

  Previously, the attachments for leaf bundles in non-multilang setups were required to be in a `files` subdirectory. For page bundles and leaf bundles in multilang setups they were always required to be in a `_index.<LANGCODE>.files` or `index.<LANGCODE>.files` subdirectory accordingly.

  This added unnessessary complexity. So attachments for leaf bundles in non-multilang setups can now also reside in a `index.files` directory. Although the old `files` directory is now deprecated, if both directories are present, only the old `files` directory will be used for compatiblity.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Absolute links prefixed with `http://` or `https://` are now opened in a separate browser tab.

  You can revert back to the old behavior by defining `externalLinkTarget="_self"` in the `params` section of your `config.toml`.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The theme now supports [Hugo's module system](https://gohugo.io/hugo-modules/).

---

## 5.8.0 (2022-12-08)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The new [`badge` shortcode]({{% relref "shortcodes/badge" %}}) is now available to add highly configurable markers to your content as you can see it on this page.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The new [`icon` shortcode]({{% relref "shortcodes/icon" %}}) simplyfies the usage of icons. This can even be combined with also new `badge` shortcode.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The theme now supports some of GFM (GitHub Flavored Markdown) syntax and Hugo Markdown extensions, namely [task lists]({{% relref "cont/markdown#tasks" %}}), [defintion lists]({{% relref "cont/markdown#defintions" %}}) and [footnotes]({{% relref "cont/markdown#footnotes" %}}).

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} A new color `--ACCENT-color` was introduced which is used for highlightning search results on the page. In case you simply don't care, you don't need to change anything in your variant stylesheet as the old `yellow` color is still used as default.

---

## 5.7.0 (2022-11-29)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The Korean language translation for this theme is now available with the language code `ko`. Formerly the country code `kr` was used instead.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The [`button` shortcode]({{% relref "shortcodes/button" %}}) can now also be used as a real button inside of HTML forms - although this is a pretty rare use case. The documentation was updated accordingly.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The search now supports the Korean language.

---

## 5.6.0 (2022-11-18)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} This release introduces an additional dedicated search page. On this page, displayed search results have more space making it easier scanning thru large number of results.

  To activate this feature, you need to [configure it]({{% relref "basics/configuration#activate-dedicated-search-page" %}}) in your `config.toml` as a new outputformat `SEARCHPAGE` for the home page. If you don't configure it, no dedicated search page will be accessible and the theme works as before.

  You can access the search page by either clicking on the magnifier glass or pressing enter inside of the search box.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Keyboard handling for the TOC and search was improved.

  Pressing `CTRL+ALT+t` now will not only toggle the TOC overlay but also places the focus to the first heading on opening. Subsequently this makes it possible to easily select headings by using the `TAB` key.

  The search received its own brand new keyboard shortcut `CTRL+ALT+f`. This will focus the cursor inside of the the search box so you can immediately start your search by typing.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} You are now able to turn off the generation of generator meta tags in your HTML head to hide the used versions of Hugo and this theme.

  To [configure this]({{% relref "basics/configuration#global-site-parameters" %}}) in your `config.toml` make sure to set Hugo's `disableHugoGeneratorInject=true` **and** also `[params] disableGeneratorVersion=true`, otherwise Hugo will generate a meta tag into your home page automagically.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Creation of your project gets a little bit faster with this release.

  This addresses increased build time with the 5.x releases. The theme now heavily caches partial results leading to improved performance. To further increase performance, unnecessary parts of the page are now skipped for creation of the print output (eg. menus, navigation bar, etc.).

---

## 5.5.0 (2022-11-06)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The way images are processed has changed. Now images are lazy loaded by default which speeds up page load on slow networks and/or big pages and also the print preview.

  For that the JavaScript code to handle the [lightbox and image effects]({{% relref "cont/markdown#further-image-formatting" %}}) on the client side was removed in favour for static generation of those effects on the server.

  If you have used HTML directly in your Markdown files, this now has the downside that it doesn't respect the effect query parameter anymore. In this case you have to migrate all your HTML `img` URLs manually to the respective HTML attributes.

  | Old                                                    | New                                                             |
  | ------------------------------------------------------ | --------------------------------------------------------------- |
  | `<img src="pic.png?width=20vw&classes=shadow,border">` | `<img src="pic.png" style="width:20vw;" class="shadow border">` |

---

## 5.4.0 (2022-11-01)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} [With the proper settings]({{% relref "basics/configuration#serving-your-page-from-the-filesystem" %}}) in your `config.toml` your page is now servable from the local file system using `file://` URLs.

  Please note that the searchbox will only work for this if you reconfigure your outputformat for the homepage in your `config.toml` from `JSON` to `SEARCH`. The now deprecated `JSON` outputformat still works as before, so there is no need to reconfigure your installation if it is only served from `http://` or `https://`.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The [`button` shortcode]({{% relref "shortcodes/button" %}}) has a new parameter `target` to set the destination frame/window for the URL to open. If not given, it defaults to a new window/tab for external URLs or is not set at all for internal URLs. Previously even internal URLs where opened in a new window/tab.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The [`math` shortcode]({{% relref "shortcodes/math" %}}) and [`mermaid` shortcode]({{% relref "shortcodes/mermaid" %}}) now also support the `align` parameter if codefence syntax is used.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Support for languages that are written right to left (like Arabic). This is only implemented for the content area but not the navigation sidebar. This feature is not available in Internet Explorer 11.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Translation for Finnish (Suomi).

---

## 5.3.0 (2022-10-07)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} In the effort to comply with WCAG standards, the implementation of the collapsible menu was changed. The functionality of the new implementation does not work with old browsers (Internet Explorer 11).

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} [Image formatting]({{% relref "cont/markdown#add-css-classes" %}}) has two new classes to align images to the `left` or `right`. Additionally, the already existing `inline` option is now documented.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Printing for the [`swagger` shortcode]({{% relref "shortcodes/swagger" %}}) was optimized to expand sections that are usually closed in interactive mode. This requires [print support]({{%relref "basics/configuration#activate-print-support" %}}) to be configured.

---

## 5.2.0 (2022-08-03)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} If you've set `collapsibleMenu = true` in your `config.toml`, the menu will be expanded if a search term is found in a collapsed submenu. The menu will return to its initial collapse state once the search term does not match any submenus.

---

## 5.1.0 (2022-07-15)

- {{% badge color="fuchsia" icon="fab fa-hackerrank" title=" " %}}0.95.0{{% /badge %}} This release requires a newer Hugo version.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Because the print preview URLs were non deterministic for normal pages in comparison to page bundles, this is now changed. Each print preview is now accessible by adding a `index.print.html` to the default URL.

  You can revert this behavior by overwriting the PRINT output format setting in your `config.toml`to:

  ````toml
  [outputFormats]
    [outputFormats.PRINT]
      name= "PRINT"
      baseName = "index"
      path = "_print"
      isHTML = true
      mediaType = 'text/html'
      permalinkable = false
  ````

---

## 5.0.0 (2022-07-05)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} The theme changed how JavaScript and CSS dependencies are loaded to provide a better performance. In case you've added own JavaScript code that depends on the themes jQuery implementation, you have to put it into a separate `*.js` file (if not already) and add the `defer` keyword to the `script` element. Eg.

  ````html
  <script defer src="myscript.js"></script>
  ````

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The way [archetypes]({{% relref "cont/archetypes" %}}) are used to generate output has changed. The new systems allows you, to redefine existing archetypes or even generate your own ones.

  Your existing markdown files will still work like before and therefore you don't need to change anything after the upgrade. Nevertheless, it is recommended to adapt your existing markdown files to the new way as follows:

  - for your home page, add the frontmatter parameter `archetype = "home"` and remove the leading heading

  - for all files containing the deprecated frontmatter parameter `chapter = true`, replace it with `archetype = "chapter"` and remove the leading headings

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The frontmatter options `pre` / `post` were renamed to `menuPre` / `menuPost`. The old options will still be used if the new options aren't set. Therefore you don't need to change anything after the upgrade.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Adding new partials `heading-pre.html` / `heading-post.html` and according frontmatter options `headingPre` / `headingPost` to modify the way your page`s main heading gets styled.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The new shortcode `math` is available to add beautiful math and chemical formulae. See the [documentation]({{% relref "shortcodes/math" %}}) for available features. This feature will not work with Internet Explorer 11.

---

## 4.2.0 (2022-06-23)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} The second parameter for the [`include` shortcode]({{% relref "shortcodes/include" %}}) was switched in meaning and was renamed from `showfirstheading` to `hidefirstheading`. If you haven't used this parameter in your shortcode, the default behavior hasn't changed and you don't need to change anything.

  If you've used the second boolean parameter, you have to rename it and invert its value to achieve the same behavior.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Previously, if the [`tabs` shortcode]({{% relref "shortcodes/tabs" %}}) could not find a tab item because, the tabs ended up empty. Now the first tab is selected instead.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} The `landingPageURL` was removed from `config.toml`. You can safely remove this as well from your configuration as it is not used anymore. The theme will detect the landing page URL automatically.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} All shortcodes can now be also called from your partials. Examples for this are added to the documentation of each shortcode.

---

## 4.1.0 (2022-06-12)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} While fixing issues with the search functionality for non Latin languages, you can now [configure to have multiple languages on a single page]({{% relref "cont/i18n/#search-with-mixed-language-support" %}}).

---

## 4.0.0 (2022-06-05)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} The `custom_css` config parameter was removed from the configuration. If used in an existing installation, it can be achieved by overriding the `custom-header.html` template in a much more generic manner.

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} Because anchor hover color was not configurable without introducing more complexity to the variant stylesheets, we decided to remove `--MAIN-ANCHOR-color` instead. You don't need to change anything in your custom color stylesheet as the anchors now get their colors from `--MAIN-LINK-color` and `--MAIN-ANCHOR-HOVER-color` respectively.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} All shortcodes now support named parameter. The positional parameter are still supported but will not be enhanced with new features, so you don't need to change anything in your installation.

  This applies to [`expand`]({{% relref "shortcodes/expand" %}}), [`include`]({{% relref "shortcodes/include" %}}), [`notice`]({{% relref "shortcodes/notice" %}}) and [`siteparam`]({{% relref "shortcodes/siteparam" %}}).

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The [`button`]({{% relref "shortcodes/button" %}}) shortcode received some love and now has a parameter for the color style similar to other shortcodes.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} New colors `--PRIMARY-color` and `--SECONDARY-color` were added to provide easier modification of your custom style. Shortcodes with a color style can now have `primary` or `secondary` as additional values.

  These two colors are the default for other, more specific color variables. You don't need to change anything in your existing custom color stylesheets as those variables get reasonable default values.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Translation for Polish. This language is not supported for search.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The documentation for all shortcodes were revised.

---

## 3.4.0 (2022-04-03)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} If you had previously overwritten the `custom-footer.html` partial to add visual elements below the content of your page, you have to move this content to the new partial `content-footer.html`. `custom-footer.html` was never meant to contain HTML other than additional styles and JavaScript.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} If you prefer expandable/collapsible menu items, you can now set `collapsibleMenu=true` in your `config.toml`. This will add arrows to all menu items that contain sub menus. The menu will expand/collapse without navigation if you click on an arrow.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} You can activate [print support]({{%relref "basics/configuration#activate-print-support" %}}) in your `config.toml` to add the capability to print whole chapters or even the complete site.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Translation for Traditional Chinese.

---

## 3.3.0 (2022-03-28)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Introduction of new CSS variables to set the font. The theme distinguishes between `--MAIN-font` for all content text and `--CODE-font` for inline or block code. There are additional overrides for all headings. See the [theme variant generator]({{%relref "basics/generator" %}}) of the exampleSite for all available variables.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The new shortcode `swagger` is available to include a UI for REST OpenAPI Specifications. See the [documentation]({{% relref "shortcodes/swagger" %}}) for available features. This feature will not work with Internet Explorer 11.

---

## 3.2.0 (2022-03-19)

- {{% badge color="fuchsia" icon="fab fa-hackerrank" title=" " %}}0.93.0{{% /badge %}} This release requires a newer Hugo version.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} In this release the Mermaid JavaScript library will only be loaded on demand if the page contains a Mermaid shortcode or is using Mermaid codefences. This changes the behavior of `disableMermaid` config option as follows: If a Mermaid shortcode or codefence is found, the option will be ignored and Mermaid will be loaded regardlessly.

  The option is still useful in case you are using scripting to set up your graph. In this case no shortcode or codefence is involved and the library is not loaded by default. In this case you can set `disableMermaid=false` in your frontmatter to force the library to be loaded. See the [theme variant generator]({{%relref "basics/generator" %}}) of the exampleSite for an example.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Additional color variant variable `--MERMAID-theme` to set the variant's Mermaid theme. This causes the Mermaid theme to switch with the color variant if it defers from the setting of the formerly selected color variant.

---

## 3.1.0 (2022-03-15)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} [`attachment`]({{% relref "shortcodes/attachments" %}}) and [`notice`]({{% relref "shortcodes/notice" %}}) shortcodes have a new parameter to override the default icon. Allowed values are all [Font Awesome 5 Free](https://fontawesome.com/v5/search?m=free) icons.

---

## 3.0.0 (2022-02-22)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} We made changes to the menu footer. If you have your `menu-footer.html` [partial overridden]({{%relref "basics/customization" %}}), you may have to review the styling (eg. margins/paddings) in your partial. For a reference take a look into the `menu-footer.html` partial that is coming with the exampleSite.

  This change was made to allow your own menu footer to be placed right after the so called prefooter that comes with the theme (containing the language switch and *Clear history* functionality).

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} We have changed the default colors from the original Learn theme (the purple menu header) to the Relearn defaults (the light green menu header) as used in the official documentation.

  This change will only affect your installation if you've not set the `themeVariant` parameter in your `config.toml`. [If you still want to use the Learn color variant]({{%relref "basics/customization/#theme-variant" %}}), you have to explicitly set `themeVariant="learn"` in your `config.toml`.

  Note, that this will also affect your site if viewed with Internet Explorer 11 but in this case it can not be reconfigured as Internet Explorer does not support CSS variables.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Due to a bug, that we couldn't fix in a general manner for color variants, we decided to remove `--MENU-SEARCH-BOX-ICONS-color` and introduced `--MENU-SEARCH-color` instead. You don't need to change anything in your custom color stylesheet as the old name will be used as a fallback.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} For consistency reasons, we renamed `--MENU-SEARCH-BOX-color` to `--MENU-SEARCH-BORDER-color`. You don't need to change anything in your custom color stylesheet as the old name will be used as a fallback.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} With this release you are now capable to define your own *dark mode* variants.

  To make this possible, we have introduced a lot more color variables you can use in [your color variants]({{%relref "basics/customization/#theme-variant" %}}). Your old variants will still work and don't need to be changed as appropriate fallback values are used by the theme. Nevertheless, the new colors allow for much more customization.

  To see what's now possible, see the new variants `relearn-dark` and `neon` that are coming with this release.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} To make the creation of new variants easier for you, we've added a new interactive [theme variant generator]({{%relref "basics/generator" %}}). This feature will not work with Internet Explorer 11.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} You can now configure multiple color variants in your `config.toml`. In this case, the first variant is the default chosen on first view and a variant switch will be shown in the menu footer. See the [documentation]({{%relref "basics/customization/#multiple-variants" %}}) for configuration.

  Note, that the new variant switch will not work with Internet Explorer 11 as it does not support CSS variables. Therefore, the variant switcher will not be displayed with Internet Explorer 11.

---

## 2.9.0 (2021-11-19)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} This release removes the themes implementation of `ref`/`relref` in favor for Hugos standard implementation. This is because of inconsistencies with the themes implementation. In advantage, your project becomes standard compliant and exchanging this theme in your project to some other theme will be effortless.

  In a standard compliant form you must not link to the `*.md` file but to its logical name. You'll see, referencing other pages becomes much easier. All three types result in the same reference:

  | Type          | Non-Standard                     | Standard               |
  | ------------- | -------------------------------- | ---------------------- |
  | Branch bundle | `basics/configuration/_index.md` | `basics/configuration` |
  | Leaf bundle   | `basics/configuration/index.md`  | `basics/configuration` |
  | Page          | `basics/configuration.md`        | `basics/configuration` |

  If you've linked from a page of one language to a page of another language, conversion is a bit more difficult but [Hugo got you covered](https://gohugo.io/content-management/cross-references/#link-to-another-language-version) as well.

  Also, the old themes implementation allowed refs to non-existing content. This will cause Hugos implementation to show the error below and abort the generation. If your project relies on this old behavior, you can [reconfigure the error handling](https://gohugo.io/content-management/cross-references/#link-to-another-language-version) of Hugos implementation.

  In the best case your usage of the old implementation is already standard compliant and you don't need to change anything. You'll notice this very easily once you've started `hugo server` after an upgrade and no errors are written to the console.

  You may see errors on the console after the update in the form:

  ````sh
  ERROR 2021/11/19 22:29:10 [en] REF_NOT_FOUND: Ref "basics/configuration/_index.md": "hugo-theme-relearn\exampleSite\content\_index.en.md:19:22": page not found
  ````

  In this case, you must apply one of two options:

  1. Copy the old implementation files `theme/hugo-theme-relearn/layouts/shortcode/ref.html` and `theme/hugo-theme-relearn/layouts/shortcode/relref.html` to your own projects `layouts/shortcode/ref.html` and `layouts/shortcode/relref.html` respectively. **This is not recommended** as your project will still rely on non-standard behavior afterwards.

  2. Start up a text editor with regular expression support for search and replace. Apply the following conversions in the given order on all `*.md` files. **This is the recommended choice**.

    | Type          | Search                       | Replace by |
    | ------------- | ---------------------------- | ---------- |
    | Branch bundle | `(ref\s+"[^"]*)/_index\.md"` | `$1"`      |
    | Leaf bundle   | `(ref\s+"[^"]*)/index\.md"`  | `$1"`      |
    | Page          | `(ref\s+"[^"]*)\.md"`        | `$1"`      |

---

## 2.8.0 (2021-11-03)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Although never officially documented, this release removes the font `Novacento`/`Novecento`. If you use it in an overwritten CSS please replace it with `Work Sans`. This change was necessary as Novacento did not provide all Latin special characters and lead to mixed styled character text eg. for Czech.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The theme now supports favicons served from `static/images/` named as `favicon` or `logo` in SVG, PNG or ICO format [out of the box]({{% relref "basics/customization/#change-the-favicon" %}}). An overridden partial `layouts/partials/favicon.html` may not be necessary anymore in most cases.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} You can hide the table of contents menu for the whole site by setting the `disableToc` option in your `config.toml`. For an example see [the example configuration]({{%relref "basics/configuration/#global-site-parameters" %}}).

---

## 2.7.0 (2021-10-24)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Optional second parameter for [`notice`]({{% relref "shortcodes/notice" %}}) shortcode to set title in box header.

---

## 2.6.0 (2021-10-21)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Your site can now be served from a subfolder if you set `baseURL` and `canonifyURLs=true` in your `config.toml`. See the [documentation]({{% relref "basics/configuration/#a-word-on-running-your-site-in-a-subfolder" %}}) for a detailed example.

---

## 2.5.0 (2021-10-08)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} New colors `--CODE-BLOCK-color` and `--CODE-BLOCK-BG-color` were added to provide a fallback for Hugos syntax highlighting in case `guessSyntax=true` is set. Ideally the colors are set to the same values as the ones from your chosen chroma style.

---

## 2.4.0 (2021-10-07)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Creation of customized stylesheets was simplified down to only contain the CSS variables. Everything else can and should be deleted from your custom stylesheet to assure everything works fine. For the predefined stylesheet variants, this change is already included.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Hidden pages are displayed by default in their according tags page. You can now turn off this behavior by setting `disableTagHiddenPages=true` in your `config.toml`.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} You can define the expansion state of your menus for the whole site by setting the `alwaysopen` option in your `config.toml`. Please see further [documentation]({{%relref "cont/pages/#override-expand-state-rules-for-menu-entries" %}}) for possible values and default behavior.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} New frontmatter `ordersectionsby` option to change immediate children sorting in menu and `children` shortcode. Possible values are `title` or `weight`.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Alternate content of a page is now advertised in the HTML meta tags. See [Hugo documentation](https://gohugo.io/templates/rss/#reference-your-rss-feed-in-head).

---

## 2.3.0 (2021-09-13)

- {{% badge color="fuchsia" icon="fab fa-hackerrank" title=" " %}}0.81.0{{% /badge %}} This release requires a newer Hugo version.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Showcase multilanguage features by providing a documentation translation "fer us pirrrates". There will be no other translations besides the original English one and the Pirates one due to maintenance constraints.

---

## 2.2.0 (2021-09-09)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Hidden pages are displayed by default in the sitemap generated by Hugo and are therefore visible for search engine indexing. You can now turn off this behavior by setting `disableSeoHiddenPages=true` in your `config.toml`.

---

## 2.1.0 (2021-09-07)

- {{% badge color="fuchsia" icon="fab fa-hackerrank" title=" " %}}0.69.0{{% /badge %}} This release requires a newer Hugo version.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} In case the site's structure contains additional *.md files not part of the site (eg files that are meant to be included by site pages - see `CHANGELOG.md` in the exampleSite), they will now be ignored by the search.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Hidden pages are indexed for the site search by default. You can now turn off this behavior by setting `disableSearchHiddenPages=true` in your `config.toml`.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} If a search term is found in an `expand` shortcode, the expand will be opened.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} The menu will scroll the active item into view on load.

---

## 2.0.0 (2021-08-28)

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Syntax highlighting was switched to the [built in Hugo mechanism](https://gohugo.io/content-management/syntax-highlighting/). You may need to configure a new stylesheet or decide to roll you own as described on in the Hugo documentation

- {{% badge style="note" title=" " %}}Change{{% /badge %}} In the predefined stylesheets there was a typo and `--MENU-HOME-LINK-HOVERED-color` must be changed to `--MENU-HOME-LINK-HOVER-color`. You don't need to change anything in your custom color stylesheet as the old name will be used as a fallback.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} `--MENU-HOME-LINK-color` and `--MENU-HOME-LINK-HOVER-color` were missing in the documentation. You should add them to your custom stylesheets if you want to override the defaults.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} Arrow navigation and `children` shortcode were ignoring setting for `ordersectionsby`. This is now changed and may result in different sorting order of your sub pages.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} If hidden pages are accessed directly by typing their URL, they will be exposed in the menu.

- {{% badge style="note" title=" " %}}Change{{% /badge %}} A page without a `title` will be treated as `hidden=true`.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} You can define the expansion state of your menus in the frontmatter. Please see further [documentation]({{%relref "cont/pages/#override-expand-state-rules-for-menu-entries" %}}) for possible values and default behavior.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} New partials for defining pre/post content for menu items and the content. See [documentation]({{% relref "basics/customization" %}}) for further reading.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Shortcode [`children`]({{% relref "shortcodes/children" %}}) with new parameter `containerstyle`.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} New shortcode [`include`]({{% relref "shortcodes/include" %}}) to include arbitrary file content into a page.

---

## 1.2.0 (2021-07-26)

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Shortcode [`expand`]({{% relref "shortcodes/expand" %}}) with new parameter to open on page load.

---

## 1.1.0 (2021-07-02)

- {{% badge style="warning" title=" " %}}Breaking{{% /badge %}} [Mermaid]({{% relref "shortcodes/mermaid" %}}) diagrams can now be panned and zoomed. This isn't configurable yet.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} [`Mermaid`]({{% relref "shortcodes/mermaid#configuration" %}}) config options can be set in `config.toml`.

---

## 1.0.0 (2021-07-01)

- {{% badge color="fuchsia" icon="fab fa-hackerrank" title=" " %}}0.65.0{{% /badge %}} The requirement for the Hugo version of this theme is the same as for the Learn theme version 2.5.0 on 2021-07-01.

- {{% badge style="info" icon="plus-circle" title=" " %}}New{{% /badge %}} Initial fork of the [Learn theme](https://github.com/matcornic/hugo-theme-learn) based on Learn 2.5.0 on 2021-07-01. This introduces no new features besides a global rename to `Relearn` and a new logo. For the reasons behind forking the Learn theme, see [this comment](https://github.com/matcornic/hugo-theme-learn/issues/442#issuecomment-907863495) in the Learn issues.
