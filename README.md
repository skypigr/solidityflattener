# Solidity Flattener

**Are you tired of having to manually combine all of your files** when verifying your contract source on [Etherscan](https://etherscan.io)? This script automatically traverses the dependency graph and outputs all of your imports in the correct order, ready to be pasted into the contract verifier.

This is also useful for quickly throwing your source into [Remix](https://ethereum.github.io/browser-solidity/) without having to fumble with local filesystem connections.


# Requirements

* Python 3.5+


# Usage
```
usage: python solidityflattener source_solidity_file.sol target_solidity_file.sol

Flattens a target Solidity source file by resolving all of its imports and
dependencies. NOTE: This does not work with imports that are aliased (i.e.
import './A.sol' as B; )

```

# Examples

To flatten a Solidity file:

`python solidityflattener StandardToken.sol StandardTokenFlattened.sol`


# Contributions

Pull requests are welcome, or feel free to open an issue to discuss.
