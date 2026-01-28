console.log("CardioCare AI Loaded");
console.log("CardioCare AI UI Loaded");

document.querySelectorAll("input, select").forEach(el=>{
  el.addEventListener("focus",()=>el.style.boxShadow="0 0 0 2px rgba(0,212,255,0.3)");
  el.addEventListener("blur",()=>el.style.boxShadow="none");
});
