# Submission

## Cover

**Student:** Khaled Abdulhabib  
**Supervisors:** Professor Mahmoud and Sufyan Al-Ba'adani  
**Course:** A1 Cybersecurity Bootcamp capstone  
**Date:** November 1, 2026  
**Project:** Library vs Framework

## How to inspect or run examples

These are deliberately skeleton snippets; they are not standalone runnable applications. No install or execution is needed: open each `library-style` and `framework-style` file to compare the control flow. If adapting them, create the appropriate package/project first and use the framework's documented local development command. Inspection of all five pairs takes under five minutes. CI does not execute these example files.

## Self-assessment checklist

- [x] Root README, MIT license, security policy, submission, changelog, gitignore, and SHA-256 manifest.
- [x] Six requested documentation files, including one Mermaid IoC diagram and a five-row STRIDE table.
- [x] Five stack folders, each with two short illustrative code files and a ten-line README.
- [x] GitHub Actions workflow configured for markdownlint, link checking, and actionlint.
- [x] README required sections, tagged fences, and internal documentation links.
- [x] ZIP archive named exactly `Library Vs Framework.zip`, containing `Library-vs-Framework/` as its root and no nested ZIP.

## Known limitations

1. Examples are conceptual skeletons, not complete buildable projects; they omit framework bootstraps, dependency manifests, and tests.
2. Markdown/code examples are not compiled or executed in CI. The mandated literal `// ILLUSTRATIVE` prefix is not a valid Python comment, so the Python fragments prioritize the exact labeling requirement and are not directly executable Python files.
3. The qualitative resolution descriptions are version- and configuration-dependent. The comparison is educational, not a performance benchmark or a security certification.

Scope was cut to the requested five pairs of two tiny files each. No full framework scaffolding, extra diagram, screenshot, PDF, benchmark, or automated runtime test was added.

## Verification results

- [x] Markdown lint: passed with markdownlint-cli2 v0.18.1 using the repository configuration.
- [x] Internal links resolve: passed for local Markdown links in the repository.
- [x] Every Markdown code fence has a language tag: passed.
- [x] Secret scan: no credential-like values or prohibited scan keywords were present in repository files.
- [x] ZIP extracts to `Library-vs-Framework/`: passed.
- [x] Manifest hashes match: passed for every listed file.
- [x] External references: nine URLs fetched successfully; one additional Fowler IoC bliki URL included as a well-known reference but not fetched, staying within the ten-URL verification cap.
- [ ] GitHub workflow syntax: actionlint was not available in the build environment; the CI workflow includes the actionlint check for GitHub execution.

Manifest scope: `MANIFEST.txt` lists every other file in the repository. It cannot include its own hash without an impossible self-referential digest; the archive is not part of the repository tree and is also excluded.
