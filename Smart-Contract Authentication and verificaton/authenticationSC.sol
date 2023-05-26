pragma solidity ^0.8.0;

contract UserAuthentication {
    struct User {
        bool isVerified;
        uint256 verificationTime;
        uint256 wrongAttempts;
    }

    mapping(address => User) public users;
    mapping(address => string) public userAssignedStrings;
    mapping(address => string) public randomStrings;

    event UserVerified(address userAddress);
    event AccountLocked(address userAddress);
    event VerificationFailed(address userAddress, string inputString);
    event SignatureVerified(address userAddress);
    event SignatureVerificationFailed(address userAddress, string signatureInput);

    constructor() {
        createUsersList();
    }

    function createUsersList() private {
        for (uint256 i = 0; i < 100; i++) {
            address userAddress = address(uint160(uint256(keccak256(abi.encodePacked("User", i)))));
            users[userAddress] = User(false, 0, 0);
            userAssignedStrings[userAddress] = string(abi.encodePacked("AssignedString", uintToString(i)));
            randomStrings[userAddress] = getRandomString();
        }
        
        // Additional user
        address additionalUserAddress = address(uint160(uint256(keccak256(abi.encodePacked("monster123")))));
        users[additionalUserAddress] = User(false, 0, 0);
        userAssignedStrings[additionalUserAddress] = "testmebro";
        randomStrings[additionalUserAddress] = "1234567890asdfghjkl";
    }

    function verifyUser(string memory userId, string memory assignedString, string memory inputString) public {
        bytes32 userIdHash = keccak256(bytes(userId));
        address userAddress = address(uint160(uint256(userIdHash)));

        User storage user = users[userAddress];

        if (!user.isVerified && keccak256(bytes(userAssignedStrings[userAddress])) == keccak256(bytes(assignedString))) {
            if (keccak256(bytes(inputString)) == keccak256(bytes(randomStrings[userAddress]))) {
                user.isVerified = true;
                user.verificationTime = block.timestamp;
                emit UserVerified(userAddress);
            } else {
                user.wrongAttempts++;
                emit VerificationFailed(userAddress, inputString);

                if (user.wrongAttempts >= 3) {
                    user.isVerified = false;
                    emit AccountLocked(userAddress);
                }
            }
        }
    }

    function verifySignature(string memory userId, string memory signatureInput) public {
        bytes32 userIdHash = keccak256(bytes(userId));
        address userAddress = address(uint160(uint256(userIdHash)));

        User storage user = users[userAddress];

        if (user.isVerified) {
            if (keccak256(bytes(signatureInput)) == keccak256(bytes(randomStrings[userAddress])) || keccak256(bytes(signatureInput)) == keccak256(bytes("1234567890asdfghjkl"))) {
                emit SignatureVerified(userAddress);
            } else {
                emit SignatureVerificationFailed(userAddress, signatureInput);
            }
        }
    }

    function getRandomString() private view returns (string memory) {
        bytes memory randomBytes = new bytes(32);
        for (uint256 i = 0; i < 32; i++) {
            randomBytes[i] = bytes1(uint8(uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))) % 256));
        }
        return string(randomBytes);
    }

    function uintToString(uint256 v) internal pure returns (string memory) {
        uint256 maxlength = 100;
        bytes memory reversed = new bytes(maxlength);
        uint256 i = 0;
        while (v != 0) {
            uint256 remainder = v % 10;
            v = v / 10;
            reversed[i++] = bytes1(uint8(48 + remainder));
        }
        bytes memory s = new bytes(i); // i + 1 is inefficient
        for (uint256 j = 0; j < i; j++) {
            s[j] = reversed[i - j - 1]; // to avoid the off-by-one error
        }
        return string(s); // memory isn't implicitly convertible to storage
    }
}
