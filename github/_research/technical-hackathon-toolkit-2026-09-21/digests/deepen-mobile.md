# Deepen: Mobile app demo at a hackathon (Sep 2026)

Run budget: 12 tool calls, one round. Every claim below comes from pages fetched or search results retrieved on 2026-09-22. Classes: F = fact from a primary or official source, S = secondary or aggregator claim, D = derived.

## Findings

1. The latest stable Expo SDK is **SDK 57**, released 2026-06-30. **SDK 58 went to beta on 2026-09-15**, and SDK 56 came out on 2026-05-21. | https://expo.dev/changelog | Expo | 2026-09-15 (latest entry) | accessed 2026-09-22 | high | F
2. SDK 57 ships **React Native 0.86 and React 19.2**, has "no user-facing breaking changes", and starts a shift toward more frequent non-breaking SDK updates. | https://expo.dev/changelog/sdk-57 | Expo | 2026-06-30 | accessed 2026-09-22 | high | F
3. **Expo Go for SDK 57 was not on the iOS App Store: it was "still waiting on approval"** (notes updated 2026-08-13). The workarounds are `eas go` or installing through the CLI. Android Expo Go is available through the Expo CLI. | https://expo.dev/changelog/sdk-57 ; https://expo.dev/go?sdkVersion=57&platform=ios&device=true | Expo | 2026-06-30 / updated 2026-08-13 | accessed 2026-09-22 | high (status could have changed after 08-13) | F
4. `eas go` builds Expo Go for your chosen SDK on EAS, submits it to App Store Connect, and delivers it to your **TestFlight internal team**. It needs an Apple Developer account and App Store Connect. | https://github.com/expo/fyi/blob/main/deploy-expo-go-testflight.md (seen in search snippet) ; https://expo.dev/changelog/expo-go-and-app-store-may-2026 | Expo | 2026 | accessed 2026-09-22 | medium (snippet only, page not fetched) | S
5. Expo says "Expo Go is not recommended as a development environment for production apps". A development build is "your own version of Expo Go" where any native library or native config can be used. | https://expo.dev/changelog/sdk-57 ; https://docs.expo.dev/develop/development-builds/expo-go-to-dev-build/ | Expo | 2026 | accessed 2026-09-22 | high | F
6. You can build and run on an iPhone **without a paid Apple Developer account only through local builds**. EAS device builds imply a paid account. | https://docs.expo.dev/develop/development-builds/expo-go-to-dev-build/ | Expo docs | n.d. | accessed 2026-09-22 | medium | F
7. The EAS **Free plan includes 15 Android and 15 iOS builds per month on a low-priority queue, EAS Update to 1K MAUs, and App Store submission**. | https://expo.dev/pricing | Expo | n.d. | accessed 2026-09-22 | high | F
8. Android internal distribution: "APKs can be installed directly to an Android device over USB, by downloading the file over the web or through an email or chat app." | https://docs.expo.dev/build/internal-distribution/ | Expo docs | n.d. | accessed 2026-09-22 | high | F
9. iOS internal (ad hoc) distribution needs every device's UDID (`eas device:create`) and a paid Apple Developer account. It is capped at **100 iPhones per year**, and adding a device means rebuilding or re-signing. | https://docs.expo.dev/build/internal-distribution/ | Expo docs | n.d. | accessed 2026-09-22 | high | F
10. **React Native 0.82 was the first version to run entirely on the New Architecture.** The Legacy Architecture is deprecated or removed, and you cannot opt out in 0.82 or any later version. (Derived: SDK 57 on RN 0.86 is New-Architecture-only.) | https://reactnative.dev/blog/2025/10/08/react-native-0.82 | React Native (Meta) | 2025-10-08 | accessed 2026-09-22 | high (from search snippet of the official blog) | F
11. On iOS 26 / iPadOS 26, any site added to the Home Screen opens as a full-screen web app by default, even without a manifest. | https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide ; https://tips.ojapp.app/en/pwa-ios-2026-complete-guide/ | MagicBell / OJapp | 2026 | accessed 2026-09-22 | medium | S
12. iOS web push (16.4+) works only after the user installs the app through Safari's "Add to Home Screen", and the permission prompt must come from a user gesture. iOS still blocks Web Bluetooth, NFC, USB and background sync, and its storage quotas are tighter than Chrome's. | https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide ; https://www.mobiloud.com/blog/progressive-web-apps-ios/ | MagicBell / MobiLoud | 2026 | accessed 2026-09-22 | medium | S
13. **NativeWind v5 (Tailwind v4, react-native-css) is a pre-release or release candidate, "not intended for production use". v4 is still the stable release.** | https://www.nativewind.dev/v5 ; https://github.com/nativewind/nativewind/releases | NativeWind | 2026 | accessed 2026-09-22 | medium-high (search snippet of official docs) | F
14. React Native Reusables is a shadcn/ui-style library built on NativeWind and Radix-style primitives. gluestack-ui offers copy-paste, unstyled, accessible universal components with Tailwind-like props. Tamagui is a compiler-driven UI kit and styling system that needs more upfront setup. HeroUI Native is a React Native UI library from heroui-inc. | https://blog.logrocket.com/best-react-native-ui-component-libraries/ ; https://useaxentix.com/blog/tamagui/tamagui-gluestack-ui-kitten-what-react-native-devs-say/ ; https://github.com/heroui-inc/heroui-native | LogRocket / Axentix / heroui-inc | 2026 | accessed 2026-09-22 | medium | S
15. A commonly suggested 2026 default is NativeWind for styling, React Native Reusables or gluestack-ui for base components, and Reanimated with Gesture Handler for motion. | https://blog.logrocket.com/best-react-native-ui-component-libraries/ | LogRocket | 2026 | accessed 2026-09-22 | low-medium | S
16. Supabase has an official Expo React Native quickstart built on `@supabase/supabase-js` plus session-storage and URL-polyfill dependencies. It also has a user-management tutorial. | https://supabase.com/docs/guides/getting-started/quickstarts/expo-react-native | Supabase | n.d. | accessed 2026-09-22 | medium (snippet) | F
17. **`@clerk/clerk-expo` is deprecated. Use `@clerk/expo` (Core 3).** It offers hosted auth in a browser session, native SwiftUI or Jetpack Compose components that **require a development build**, and custom flows built with hooks. There is an official quickstart and a companion repo. | https://www.npmjs.com/package/@clerk/clerk-expo ; https://clerk.com/docs/expo/getting-started/quickstart ; https://github.com/clerk/clerk-expo-quickstart | Clerk | 2026 | accessed 2026-09-22 | medium-high | F
18. Lynx (ByteDance) was open-sourced on 2025-03-05. ReactLynx is a Preact-based React implementation with a dual-thread model. Secondary sources call its ecosystem and tooling early outside ByteDance. One source says it is "embedded-only" and cannot scaffold a standalone app; this is unverified against lynxjs.org. | https://lynxjs.org/ ; https://www.pkgpulse.com/guides/lynx-bytedance-framework-vs-react-native-2026 | ByteDance / PkgPulse | 2025–2026 | accessed 2026-09-22 | low-medium | S

## Recommended hackathon stack (derived)

- **Default: Expo SDK 57 (stable), not the SDK 58 beta** (F1, F2). Everything runs on the New Architecture, so check that any native library you add supports it (F10).
- **Getting it onto judges' phones:**
  - **Android:** build an APK with the EAS internal profile and share a link or QR code. There is no account or device registration friction (F7, F8). This is the fastest path.
  - **iOS:** Expo Go for the current SDK may still be missing from the App Store (F3). Ad hoc builds need UDIDs collected in advance and a paid account (F9). A TestFlight internal team or `eas go` also needs Apple accounts and processing time (F4).
  - **Practical fallback:** run the demo on your own iPhone with a development build, or show a web build (next point).
  - **Build early:** the free tier queue is low-priority, so an early build avoids waiting in line (F7). EAS Update covers last-minute JS fixes for up to 1K MAUs (F7).
- **Also ship a web or PWA build.** Expo can target web, and on iOS 26 "Add to Home Screen" gives a full-screen app experience with no install friction (F11). Avoid needing Bluetooth, NFC or background sync (F12).
- **UI:** use NativeWind **v4 stable** (F13) with React Native Reusables (shadcn-style) or gluestack-ui (F14, F15). Only adopt Tamagui if you already know it (F14).
- **Backend and auth:** use Supabase via supabase-js (F16). If you use Clerk, pick `@clerk/expo` with hosted auth so Expo Go / web keeps working, because native components force a dev build (F17).
- **Skip Lynx for a hackathon** because of its early ecosystem and possible embedding constraint (F18). Flutter was not researched this run.

## Repo candidates

| category | exact owner/repo slug | hackathon use | evidence URL |
|---|---|---|---|
| Expo tooling | expo/fyi | Guide for deploying Expo Go to TestFlight with `eas go` | https://github.com/expo/fyi/blob/main/deploy-expo-go-testflight.md |
| Expo tooling | expo/testflight | Ship to TestFlight from the command line with EAS Build and Submit | https://github.com/expo/testflight |
| Styling | nativewind/nativewind | Tailwind for RN (use v4 stable) | https://github.com/nativewind/nativewind/releases |
| UI kit | heroui-inc/heroui-native | Ready-made RN component library | https://github.com/heroui-inc/heroui-native |
| Auth | clerk/clerk-expo-quickstart | Official Clerk and Expo starter | https://github.com/clerk/clerk-expo-quickstart |

Warning: `bytedance/lynx` on GitHub is a video-generation research project, **not** the Lynx UI framework. Use https://lynxjs.org/ instead.

## Not found

- Whether the SDK 57 Expo Go build was approved on the App Store after 2026-08-13. Unknown.
- SDK 58 stable release date. Only the beta (2026-09-15) was found.
- The exact current create-expo-app default template and Expo Router version. Not evidenced; believed to be an Expo Router template, but unverified.
- TestFlight processing and review timelines. Not retrieved.
- Repo slugs for React Native Reusables, gluestack-ui and Tamagui. Not evidenced this run.
- HeroUI Native maturity or version.
- Flutter. No research done this run.
