function toggleTabs (target){

    const details = document.getElementById("details");
    const description = document.getElementById("description");
    

    // create a list of all tabs and iterate over it
    const array = [details, description]

    array.forEach((element) => {
        if (target !== element.id){
            element.style.display = "none"
            // if condition to check if a button has got the class "active" - is highlighted
            if (document.getElementById(element.id.concat("button")).classList.contains("active")){
                document.getElementById(element.id.concat("button")).classList.remove("active")
            }
        }

    })

    // make target div visible
    document.getElementById(target).style.display = "block"
    // highlight corresponding tab button
    document.getElementById(target.concat("button")).classList.add("active")




}