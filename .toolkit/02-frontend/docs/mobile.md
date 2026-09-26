# 📱 Mobile Apps (Expo / React Native)

<!-- markdownlint-disable MD013 -->

> The fastest way to put a mobile demo in judges' hands. From the Deepen research run (2026-09-22); sources are in [`evidence.md`](evidence.md) under "Mobile".

---

## Decision: do you need a native app at all?

| If the demo needs… | Ship |
| --- | --- |
| Screens, forms, camera/photo upload, maps | **A web app / PWA.** On iOS 26, "Add to Home Screen" opens full-screen by default. Zero install friction |
| Native APIs, smooth gestures, push, "it's an app" credibility | **Expo (React Native)**, and also ship the web build as a fallback |
| Bluetooth, NFC, background sync on iPhone | **Native (Expo dev build).** iOS PWAs still block these |

---

## The default stack

| Layer | Pick | Notes |
| --- | --- | --- |
| Framework | **Expo SDK 57** (React Native 0.86, React 19.2) | ⚠️ Don't use the SDK 58 **beta** (2026-09-15) at a hackathon |
| Architecture | New Architecture (mandatory since RN 0.82) | Check that every native library supports it |
| Styling | **NativeWind v4** (Tailwind for RN) | v5 is pre-release, "not intended for production" |
| Components | **React Native Reusables** (shadcn-style) or **gluestack-ui** | Tamagui only if you already know it; HeroUI Native is also an option |
| Motion | react-native-reanimated + gesture-handler | — |
| Backend | Supabase via `supabase-js` (official Expo quickstart) | Same RLS rules as web |
| Auth | **`@clerk/expo`** (`@clerk/clerk-expo` is deprecated) | Native Clerk components need a **development build**; hosted auth works in Expo Go and web |

---

## Getting it onto judges' phones

| Platform | Fastest path | Friction |
| --- | --- | --- |
| **Android** | EAS **internal** build → **APK link or QR** → install | Almost none: no account or device registration |
| **iOS** | Run it on **your own iPhone** (development build), or show the **web build** | Expo Go for SDK 57 was still awaiting App Store approval as of 2026-08-13. Ad hoc builds need every judge's UDID and a paid account (100 devices/year). TestFlight needs Apple accounts and processing time |
| **Everyone** | Web / PWA URL | Nothing to install |

**EAS Free plan:** 15 Android + 15 iOS builds a month on a **low-priority queue**, so start your first build early. EAS Update pushes last-minute JavaScript fixes (up to 1K MAUs).

### Checklist

- [ ] First EAS build within the first few hours (queue times vary)
- [ ] Android APK QR code on the title slide
- [ ] iOS: demo on your own device and have the web build ready
- [ ] EAS Update channel set up for hotfixes
- [ ] Backup video recorded on a real device

---

## Repos

| Repo | ⭐ | Use |
| --- | --- | --- |
| [tamagui/tamagui](https://github.com/tamagui/tamagui) | 14.2k | Universal UI kit + compiler |
| [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated) | 11.0k | Animations |
| [founded-labs/react-native-reusables](https://github.com/founded-labs/react-native-reusables) | 8.7k | shadcn-style components |
| [nativewind/nativewind](https://github.com/nativewind/nativewind) | 8.1k | Tailwind for RN (v4) |
| [gluestack/gluestack-ui](https://github.com/gluestack/gluestack-ui) | 5.3k | Accessible universal components |
| [heroui-inc/heroui-native](https://github.com/heroui-inc/heroui-native) | 3.7k | HeroUI for RN |

Checked through the GitHub API on 2026-09-22. The `expo/expo` lookup timed out, so its stars are unverified this run. Flutter wasn't researched.

## Prompt

```text
MOBILE-1 · Scaffold: Create an Expo SDK 57 app (Expo Router) with NativeWind v4 and React Native Reusables, Supabase auth + one table with RLS, and the demo screen from docs/design.md. Configure eas.json with an Android "preview" internal profile (APK) and an EAS Update channel. Also make `npx expo export --platform web` work as the fallback demo.
```
