$(document).ready(function (){
    $("#id_suppliers").change(function (){
        if($("#id_suppliers").val()==='Add Supplier'){
            console.log("Add Input")
            $("#customsupplierid").attr("type","text")
        }
        else {
            $("#customsupplierid").attr("type","hidden")
        }
    })
    $("#id_category").change(function (){
        if($("#id_category").val()==='Add Category'){
            console.log("Add Input")
            $("#customcategoryid").attr("type","text")
        }
        else {
            $("#customcategoryid").attr("type","hidden")
        }
    })
    $("#id_hasMajorAllergens").change(function (){
        if($("#id_hasMajorAllergens").val()==='true'){
            console.log("True")
            $("#display-major-allergens").css("visibility","visible")
            //$("#display-major-allergens").css("display","block")
        }
        else {
            console.log("False")
            $("#display-major-allergens").css("visibility","hidden")
            //$("#display-major-allergens").css("display","none")
        }
    })
})