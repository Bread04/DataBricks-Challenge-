# ⛓️ Web3 Stack (ETHGlobal-style hackathons)

<!-- markdownlint-disable MD013 -->

> The fastest credible dApp stack as of September 2026. From the Deepen research run (2026-09-22); sources are in [`evidence.md`](evidence.md) under "Web3". Event rules (AI disclosure, git history, video) are in [`../../01-hackathon-playbook/docs/rules-and-standards.md`](../../01-hackathon-playbook/docs/rules-and-standards.md).

---

## The default stack

| Layer | Pick | Why |
| --- | --- | --- |
| **Starter** | **Scaffold-ETH 2**: `npx create-eth@latest` → `yarn chain` · `yarn deploy` · `yarn start` | Next.js + wagmi + viem + RainbowKit already wired, hot contract reload, and you choose Foundry or Hardhat at setup |
| **Contracts toolchain** | **Foundry** or **Hardhat 3**: use the one the team knows | Hardhat 3 is stable (2026-06), with Solidity tests, fuzzing and Foundry interop (a vendor claim). No source was found recommending one over the other |
| **Contract code** | **OpenZeppelin Contracts 5.x** via the [Wizard](https://wizard.openzeppelin.com) | Audited building blocks; don't hand-roll tokens or access control |
| **Frontend client** | **viem + wagmi** | TypeScript-first; ethers v6 only if a partner SDK needs it |
| **Wallet UI** | RainbowKit (scaffold default) or **Reown AppKit** | WalletConnect is now **Reown**, and Web3Modal is now **AppKit** |
| **Onboarding** | Privy (email/social embedded wallets) or **Base Account** (passkeys, formerly Coinbase Smart Wallet) | Judges don't have to install a wallet. Privy's free-tier MAU cap is disputed (499 vs 1,000) |
| **Network** | **Sepolia** or **Base Sepolia** | ❌ **Holesky is sunset**. Hoodi is for validators, not apps |

---

## Before the event

- [ ] **Claim testnet ETH early.** Faucets rate-limit to one claim per 12–24 h: CDP (Base Sepolia, up to 0.1 ETH/24 h), Alchemy (0.1 ETH/24 h, account needed), Google Cloud Web3 faucet (Sepolia).
- [ ] Install Foundry (`foundryup`) or Node for Hardhat; run `npx create-eth@latest` on a throwaway folder to cache dependencies. Keep it out of your submission repo if prior code is banned.
- [ ] Wallet with testnet funds on the demo laptop, plus a **fresh burner account** for judges.
- [ ] Read the sponsor prize tracks. Partner prizes are often judged on written materials alone.

## During the build

- **Testnet only.** Never deploy hackathon contracts to mainnet or put real funds at risk.
- Verify the contract on the explorer, so judges can click through to real source.
- EIP-7702 (live since Pectra, 2025-05-07) lets an EOA gain smart-account features. It's useful for gasless or batched demo flows, but only if your wallet stack supports it.
- **Demo-safe:** pre-fund the demo wallet, pre-deploy the contracts, show a transaction hash that's already confirmed as a backup, and never wait on block confirmations live if you can avoid it.

---

## Repos

| Repo | ⭐ | Use |
| --- | --- | --- |
| [scaffold-eth/scaffold-eth-2](https://github.com/scaffold-eth/scaffold-eth-2) | 2.0k | One-command dApp starter |
| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 27.2k | Audited contract library |
| [foundry-rs/foundry](https://github.com/foundry-rs/foundry) | 10.6k | forge / cast / anvil |
| [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat) | 8.5k | Hardhat 3 |
| [reown-com/appkit](https://github.com/reown-com/appkit) | 5.4k | Wallet modal (ex-Web3Modal) |
| [wevm/viem](https://github.com/wevm/viem) | 3.6k | TS Ethereum client |
| [rainbow-me/rainbowkit](https://github.com/rainbow-me/rainbowkit) | 2.8k | Wallet connect UI (last push 2026-05) |

Stars were checked through the GitHub API on 2026-09-22. wagmi (`wevm/wagmi`) timed out during the check, so it's unverified this run. The full table is in [`repos.md`](repos.md) → Web3.

## Prompt

```text
WEB3-1 · Scaffold a dApp: From Scaffold-ETH 2 (Foundry), write <Contract>.sol using OpenZeppelin 5.x (<features>), Foundry tests for the happy path + one revert, a deploy script for Base Sepolia, and a Next.js page using the scaffold's hooks to read/write it. Add a DEMO_MODE that shows a pre-recorded tx hash if the RPC is slow. Testnet only.
```
