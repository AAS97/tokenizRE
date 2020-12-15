const Broker = artifacts.require("Broker");
const TokenHolderPayer = artifacts.require("TokenHolderPayer");

module.exports = function (deployer) {
  deployer.deploy(Broker, "http://localhost:8000");
  deployer.deploy(TokenHolderPayer, "token", "TKN");
};
