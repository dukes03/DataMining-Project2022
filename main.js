
let btnSubmit = document.getElementById("btnSubmit")
var feedback = ["FavoriteField","FavoriteCamp","MostImportantThingOfDesigning"]
btnSubmit.addEventListener("click", function () {
    //ดึงค่าคำตอบ
    let FavoriteField = document.querySelector("#FavoriteField").value
    let FavoriteCamp = document.querySelector("#FavoriteCamp").value
    let MostImportantThingOfDesigning = document.querySelector("#MostImportantThingOfDesigning").value
    let Java = document.querySelector("#Java").checked + 0 // boolean  +  integer  =  integer
    let Python = document.querySelector("#Python").checked + 0
    let SQL = document.querySelector("#SQL").checked + 0
    let js = document.querySelector("#js").checked + 0
    let C = document.querySelector("#C").checked + 0

    //เช็คคำตอบว่าได้เลือกหรือไม่
    let ans = [FavoriteField,FavoriteCamp,MostImportantThingOfDesigning]

    let canSend = true;
    for (let i = 0; i < ans.length; i++) {
        const element = ans[i];
        if (element === ".") {
            canSend = false
            document.querySelector("#"+feedback[i]+"-feedback").textContent = "กรุณาเลือกคำตอบ"
            document.querySelector("#"+feedback[i]).classList.add("border-danger")
            
        }
        
    }
    //ตัวอย่างตำตอบที่ได้
    //console.log("FavoriteField: ",FavoriteField, "||FavoriteCamp :",FavoriteCamp, "||MostImportantThingOfDesigning :" ,MostImportantThingOfDesigning, " Java ", Java, "Python ", Python, "SQL ", SQL,"js ", js,"C ", C)
});
for (let i = 0; i < feedback.length; i++) {
    const element = feedback[i];
    document.querySelector("#"+element).addEventListener("change", function () {
        document.querySelector("#"+element+"-feedback").textContent = ""
        document.querySelector("#"+feedback[i]).classList.remove("border-danger")
    })
}
//border border-secondary
