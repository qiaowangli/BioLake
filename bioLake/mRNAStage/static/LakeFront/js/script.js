function ganeNameTrigger() 
{ 
    if (document.getElementById("geneName").value == "")
    {
        alert("Gene name cannot be blank")
        event.preventDefault();
    }
}