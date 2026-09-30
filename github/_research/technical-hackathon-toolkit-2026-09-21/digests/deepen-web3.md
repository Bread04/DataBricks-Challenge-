# Deepen: Web3 hackathon stack (ETHGlobal-style, Sep 2026)

Run: 2026-09-22 · 12 tool calls · single round · WebSearch/WebFetch only. Class key: P = primary/vendor source, S = secondary/aggregator. Confidence: H/M/L.

## Findings

1. Hardhat 3 is declared stable ("stable, performant, and ready for prime time"); Solidity tests and JS/TS tests share output, tracing and coverage, with gas snapshots, EIP-712 cheatcodes, inline config and HTML coverage. | https://blog.nomic.foundation/hardhat-3-is-now-stable/ | Nomic Foundation | 2026-06-01 (the date the fetch tool returned) | accessed 2026-09-22 | H | P
2. Nomic says Hardhat 3 "covers the majority of foundry's functionality (including Solidity tests, fuzzing, and invariant testing)". It ships a Foundry-interop plugin that reads forge config and remappings, plus a migration guide. The post names no default between viem and ethers. | https://blog.nomic.foundation/hardhat-3-is-now-stable/ | Nomic Foundation | 2026-06-01 | accessed 2026-09-22 | H (for what Nomic claims; the parity claim comes from the vendor) | P
3. Hardhat 3 went to beta around August 2025, with a Rust-powered EDR runtime, multichain support and Hardhat Ignition deployments. A hardhat@3.4.0 release exists. | https://hardhat.org/ ; https://newreleases.io/project/github/NomicFoundation/hardhat/release/hardhat@3.4.0 | Nomic Foundation / newreleases.io | 2025–26 | accessed 2026-09-22 | M | P/S (search snippet only)
4. Scaffold-ETH 2 stack: Next.js, RainbowKit, Foundry or Hardhat (you choose), wagmi, viem and TypeScript. It adds custom hooks wrapping wagmi, prebuilt web3 components and hot contract reload. Quickstart is `npx create-eth@latest`, then `yarn chain`, `yarn deploy`, `yarn start` (runs at localhost:3000). MIT licence. The repo has 527 commits; the latest commit date was not visible. | https://github.com/scaffold-eth/scaffold-eth-2 | scaffold-eth (GitHub) | undated | accessed 2026-09-22 | H | P
5. ethereum.org lists Scaffold-ETH 2 as a developer tool. It has extensions that act as feature starter kits (for example Scaffold Chainlink for CCIP, which appears in the ETHGlobal showcase). | https://ethereum.org/developers/tools/scaffold-eth-2/ ; https://ethglobal.com/showcase/scaffold-chainlink-pwkxb | ethereum.org / ETHGlobal | undated | accessed 2026-09-22 | M | P (snippet)
6. WalletConnect Inc. rebranded to Reown. Web3Modal is now Reown AppKit, which Reown describes as a "free, and fully open-source SDK" for wallet connection on EVM and non-EVM chains. The wallet-side SDK is WalletKit. | https://reown.com/blog/walletconnect-is-now-reown ; https://github.com/reown-com/appkit | Reown | 2024-09 (per the X post) | accessed 2026-09-22 | H | P
7. viem is described as the TypeScript-first, tree-shakeable replacement for ethers; wagmi v2 is the React-hooks layer built on viem; ethers.js v6 is "battle-tested" but "showing its age". wagmi documents ethers adapters for interop. | https://www.pkgpulse.com/guides/wagmi-vs-ethersjs-vs-viem-web3-javascript-libraries-2026 ; https://wagmi.sh/core/guides/ethers | PkgPulse / wagmi | 2026 | accessed 2026-09-22 | M | S / P
8. Holesky: EF support ended 2025-09-30, and nodes shut down about 2 weeks after Fusaka finalised on Holesky. App and smart-contract developers were told to move to **Sepolia**; staking and infrastructure teams to **Hoodi** (live since 2025-03-18). The current set is Sepolia (dApps), Hoodi (validators) and Ephemery (short-lived tests). | https://blog.ethereum.org/2025/09/01/holesky-shutdown-announcement ; https://blog.ethereum.org/2025/03/18/hoodi-holesky | Ethereum Foundation | 2025-03-18 / 2025-09-01 | accessed 2026-09-22 | H | P (via search summary)
9. Base Sepolia faucets: Coinbase Developer Platform gives up to 0.1 ETH per 24h (also USDC, EURC and cbBTC; also scriptable through `@coinbase/cdp-sdk`); Alchemy gives 0.1 ETH per 24h (free account required); QuickNode gives one drip per 12h; thirdweb and Bware give one claim per 24h. | https://docs.base.org/base-chain/network-information/network-faucets ; https://www.alchemy.com/faucets/base-sepolia | Base / Alchemy | undated | accessed 2026-09-22 | H | P
10. The Google Cloud Web3 faucet gives free Sepolia ETH. | https://cloud.google.com/application/web3/faucet/ethereum/sepolia | Google Cloud | undated | accessed 2026-09-22 | M | P (snippet)
11. Privy free tier: all core features, 50K signatures and $1M monthly transaction volume. The MAU cap is **conflicting** (sources say 499 or 1,000 MAU). Paid plans are Core at $299/mo and Scale at $499/mo. | https://www.privy.io/pricing ; https://costbench.com/software/web3-wallet-sdk/privy/ | Privy / Costbench | 2026 | accessed 2026-09-22 | M | P/S (search summary, pricing page not fetched)
12. Pectra went live on Ethereum mainnet on 2025-05-07. EIP-7702 lets an EOA add smart-contract logic without changing its address. | https://blog.ethereum.org/2025/04/23/pectra-mainnet ; https://blockeden.xyz/blog/2025/05/09/eip-7702-after-pectra/ | EF / BlockEden | 2025-04-23 / 2025-05-09 | accessed 2026-09-22 | H | P
13. Coinbase Smart Wallet is branded **Base Account** (launched 2025-07-16; same contract code). Separately, the consumer "Base App" went back to the name Coinbase Wallet in about Sep 2026. | https://www.dextools.io/tutorials/what-is-coinbase-smart-wallet-passkey-base-account-guide-2026-de ; https://www.cryptotimes.io/2026/09/11/base-app-returns-to-coinbase-wallet-a-year-after-rebranding/ | DEXTools / CryptoTimes | 2026 / 2026-09-11 | accessed 2026-09-22 | M | S
14. Dynamic Labs publishes a hackathon starter kit. It pitches built-in ETHGlobal partner tech: account abstraction, chain abstraction, onboarding and EVM networks. | https://github.com/dynamic-labs/hackathon-starter-kit | Dynamic Labs | undated | accessed 2026-09-22 | M | P (snippet; the repo was not fetched and may be stale)
15. OpenZeppelin Contracts Wizard (wizard.openzeppelin.com) builds contracts interactively from OpenZeppelin Contracts components; the docs version is 5.x. | https://docs.openzeppelin.com/contracts/5.x/wizard ; https://github.com/OpenZeppelin/contracts-wizard | OpenZeppelin | undated | accessed 2026-09-22 | H | P
16. MetaMask announced embedded wallets as part of a MetaMask Developer Platform. | https://metamask.io/news/embedded-wallets-developer-platform | MetaMask | 2026 | accessed 2026-09-22 | L (title only) | P

## Recommended hackathon stack (derived)

- **Scaffold:** `npx create-eth@latest` (Scaffold-ETH 2). You get Next.js, wagmi, viem and RainbowKit already wired, plus hot reload, and you choose Foundry or Hardhat at setup [F4, F5]. This is the fastest credible starting point we found evidence for.
- **Toolchain:** either works in 2026. Hardhat 3 is stable, has Solidity tests, and interoperates with Foundry [F1–F3]. Pick whichever the team already knows. The claim that Foundry is "more recommended" was not evidenced this run (see Not found).
- **Frontend:** viem + wagmi v2 [F7]. Wallet modal: RainbowKit (the scaffold default) [F4], or Reown AppKit if you want WalletConnect-native, multichain or non-EVM support [F6]. Use ethers v6 only if the team or a partner SDK needs it [F7].
- **Onboarding:** Privy (free tier, email/social embedded wallets) [F11], or Base Account (passkey smart wallet) when building on Base [F13]. EIP-7702 is live on mainnet for EOA smart features [F12]. Dynamic's starter kit is an alternative [F14].
- **Network:** Base Sepolia or Ethereum Sepolia. **Do not use Holesky** (sunset) [F8]. Get test ETH from the CDP, Alchemy or Google Cloud faucets [F9, F10]. Claim from faucets before the event, because of the 12–24h rate limits.
- **Security:** build from OpenZeppelin Contracts 5.x via the Wizard [F15]. Deploy to testnet only. Mainnet deploys are an unsourced best-practice judgement (not evidenced this run).

## Repo candidates

| category | exact owner/repo slug | hackathon use | evidence URL |
|---|---|---|---|
| full-stack scaffold | scaffold-eth/scaffold-eth-2 | one-command dApp starter (Next.js + wagmi/viem + RainbowKit + Foundry or Hardhat) | https://github.com/scaffold-eth/scaffold-eth-2 |
| wallet connect UI | reown-com/appkit | multichain wallet modal (formerly Web3Modal) | https://github.com/reown-com/appkit |
| contract generator | OpenZeppelin/contracts-wizard | generate audited-base ERC20/721/governor code | https://github.com/OpenZeppelin/contracts-wizard |
| embedded-wallet starter | dynamic-labs/hackathon-starter-kit | Dynamic auth + partner-tech template (freshness unverified) | https://github.com/dynamic-labs/hackathon-starter-kit |
| toolchain | NomicFoundation/hardhat | Hardhat 3 dev environment | https://newreleases.io/project/github/NomicFoundation/hardhat/release/hardhat@3.4.0 |

## Not found / unverified

- Foundry's current release or status, and any source recommending Foundry over Hardhat in 2025–26. Not searched because of the tool-call budget.
- The status of RainbowKit and ConnectKit in 2026 (maintenance, versions). RainbowKit is only evidenced as the Scaffold-ETH 2 default.
- Free-tier details for Dynamic, thirdweb and Coinbase CDP. Privy's MAU cap is conflicting (499 vs 1,000).
- Official ETHGlobal statements on recommended starter kits, partner-prize structure, or the most common chains. The only ETHGlobal evidence is a showcase page and an older Superhack prizes page link.
- The exact Holesky final shutdown date (sources say "Oct 31" or "2 weeks after Fusaka"). Nothing covers whether Sepolia faces its own sunset in 2026.
- The Scaffold-ETH 2 latest commit or release date. The fetched page did not show it.
