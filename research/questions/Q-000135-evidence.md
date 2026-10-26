# Q-000135 — Google Glass GDK versus Epson Moverio stereoscopic development

**Original observed question:** [Google glass sdk for Epson moverio](https://stackoverflow.com/questions/23477637/google-glass-sdk-for-epson-moverio), 2014, retained as Q-000135. **Reviewed:** 2026-10-26.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Question asks whether Glass GDK renders separate left/right 3D views for Epson Moverio | [Original developer discussion](https://stackoverflow.com/questions/23477637/google-glass-sdk-for-epson-moverio) | Historical question; its self-answered remarks are not official compatibility claims |
| Google Glass GDK was designed for Glass-specific APIs, not Epson's stereo renderer | [Google GDK](https://developers.google.com/glass/develop/gdk) | Legacy platform scope, not exhaustive evaluation of third-party renderers |
| Epson offers its own Android Moverio Basic Function SDK with display, camera and sensor control | [Epson SDK introduction](https://tech.moverio.epson.com/en/basic_function_sdk/developers_guide/introduction.html) | Primary manufacturer documentation, applies only to listed generations |
| Epson's modern SDK excludes older BT-350-and-earlier hardware; older models need their own SDK | [Epson SDK compatibility](https://tech.moverio.epson.com/en/basic_function_sdk/developers_guide/introduction.html) | Do not generalize modern API compatibility to 2014 hardware |
| Epson documents Unity development and stereoscopic device-specific display functions | [Epson Unity development](https://tech.moverio.epson.com/en/basic_function_sdk/developers_guide_unity/developing_apps.html) | Requires model-compatible SDK, host and plugin |

## Verification and publication gate

No Epson hardware, historic GDK APK, or stereoscopic rendering test by GlassesResearch. This answer does not assert any vendor promised a particular 2014 marker editor. **State: researched; publication pending exact public FAQ and directory proof.** Proposed anchor: `docs/faq/09-development-openness.md#does-google-glass-gdk-provide-stereoscopic-3d-for-epson-moverio`.

## Publication proof — 2026-10-26

[PR #698](https://github.com/theGreenJedi/GlassesResearch/pull/698) merged as revision `2262054aaa16529f36e768925535be576f9a17b6` after documentation, editorial, link/fragment, deploy and Lighthouse checks passed. [Production content proof #40396645760](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40396645760) succeeded: fetched the complete public FAQ `/docs/faq/09-development-openness/` (digest `4208f6df07f5`), Practical Answers directory `/docs/faq/` (digest `3f42fb3fe4bc`), and this evidence page (digest `6e5c6f83529a`) matching the deployed build. The directory links to the exact built-page anchor [published answer](https://glassesresearch.org/docs/faq/09-development-openness/#does-google-glass-gdk-provide-stereoscopic-3d-for-epson-moverio), validated by strict internal fragment checks. This proves content publication, **not** a device or SDK bench test. Registry Q-000135 was credited only after this proof; original observations and uncertainty remain intact.
