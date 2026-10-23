# H2O Cloud Discovery Client Release Process

- Releases are handled by [Release Please](https://github.com/googleapis/release-please)
[GitHub Action](https://github.com/googleapis/release-please-action) that executes on
  all commits to the default branch.
- Commits to the default branch should follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) syntax.
- If the default branch contains commits that lead to the increment of a version number Release Please
  will automatically create a PR that when merged will create a new release.
- Release PR is created by the GitHub Action bot as a draft, which means that CI checks are not automatically triggered and commits are not signed.
- To activate the PR non-bot maintainer needs re-sign the release commit.

     ```sh
      git rebase --force-rebase --gpg-sign "origin/<target branch>"
      git push --force-with-lease
    ```
