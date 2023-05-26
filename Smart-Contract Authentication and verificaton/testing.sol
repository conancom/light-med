// SPDX-License-Identifier: GPL-3.0



pragma solidity ^0.8.7;

contract StartStopUpdateExample {
    address owner; // declare variable that contain address of the owner
    //Create 2 uint variable names var1 and var 2 in the template and take a screenshot of those. (We will use this later)
    uint256 public var1;
    uint256 public var2; 
    uint256 public mod;

    constructor() public {
        //Called only once when deploy 
        //This method will set whoever is the one who deploy this contract tobe owner of this contract
        owner = msg.sender;
    }
        function showOwner() public view returns(address){
        return address(owner);
    }
    
    // Q.4 Create a function which return the sender account address
    //hint "msg.sender"
    
    function getOwner(
    ) public view returns (address) {    
        return owner;
    }


       // Defining the function
        // to set the value of the
        // first variable
    function var1Set(uint x) public
    {
        var1 = x;
    }
    

    // Q.5 Create a function which use to set the var2 and mod
    //hint similar to the function above
     function var2Set(uint y) public
    {
        var2 = y;
    }

    function modSet(uint modu) public
     {
        mod = modu;
     }


    //Example for simple function
    function addition() public view returns(uint){
        uint sum = var1 + var2;
        return sum;
    }

    //Q.6 Create a subtraction function
    //Hint Similar to Above function
    function subtraction() public view returns(uint){
        uint sub = var1 - var2;
        return sub;
    }


    //Q,7 Create modulo function
    function modulo() public view returns(uint){
        uint modul = var1 % var2;
        return modul;
    }

    //Q.8)Can the function with “require(owner==msg.sender)” be called by another user?
    function destroySmartContract (address payable _to) public {
        require(msg.sender == owner, "You are not OWNER");
        selfdestruct(_to);
    }



}
