try{
  const popUp = document.querySelector(".errorPopUp");
  const message = popUp.dataset.message;
  const category = popUp.dataset.category;
  
  if (category == "False") {
    popUp.style.top = "15%";
    popUp.style.display = "flex";
    document.querySelector(".errorMessage").innerHTML = message;
  } else if (category == "True") {
    popUp.style.top = "15%";
    popUp.style.background = "#C6EBC5";
    popUp.style.display = "flex";
    document.querySelector(".errorMessage").innerHTML = message;
    document.querySelector(".errorMessage").style.color = "#76885B";
  }
  document.querySelector(".closeLogo").addEventListener("click", () => {
    popUp.style.display = "none";
  });
}
catch(error){

  console.log(error);
}


// Gen AI logic

//Gen AI launch window
const genAiWindow= document.querySelector('.genAiContainerBox')
document.querySelector('.aiButton').addEventListener("click", () => {
 genAiWindow.style.display="flex";
 adjustChatContainerHeight() 

})

//Gen AI Close window
document.querySelector('.aiBackButton').addEventListener("click",()=>{
  genAiWindow.style.display="none"
})

// socket connection logic
var socket=io();


//chatContainer
const chatContainer= document.querySelector('.aiChatContainer');


// on user prompt
const promptSearchButton=document.querySelector("#promptSearch");
promptSearchButton.addEventListener("click", () => {
  
  const prompt=document.querySelector("#promptBox");
  socket.emit("dial_prompt",{query:prompt.value});
  // promptSearchButton.style.cursor="not-allowed";
  //Appending Prompt
  const promptContainer=document.createElement('div');
  promptContainer.innerHTML=`<div class="userPrompt">${prompt.value}</div>`
  promptContainer.setAttribute("class","userPromptContainer");
  chatContainer.appendChild(promptContainer);
  //Appending Shimmer UI
  const responseContainer=document.createElement("div");
  responseContainer.innerHTML=`<div class="aiResponse">
  <div class="w-full max-w-md p-6 bg-gray-990 rounded-lg shadow-md">
    <div class="mb-4">
      <div class="mt-4 space-y-2">
        <div class="w-full h-4 bg-gray-600 rounded animate-shimmer shimmer-bg"></div>
        <div class="w-full h-4 bg-gray-600 rounded animate-shimmer shimmer-bg"></div>
        <div class="w-5/6 h-4 bg-gray-600 rounded animate-shimmer shimmer-bg"></div>
      </div>
    </div>
  </div></div>`
  responseContainer.setAttribute("class", "aiResponseContainer")
  chatContainer.appendChild(responseContainer);
  prompt.value=""
  scrollToBottom()
  

})
socket.on('response_prompt', function(data) {
  if (data && data.response) {
    const response = data.response;
    console.log('response is emitted');
    console.log(response);
    const remarkableObject = window.remarkable;
    
    // Create a new instance of remarkable
    let md = new remarkableObject.Remarkable();
    const mdText=md.render(response)
    const aiResponseContainers=document.querySelectorAll('.aiResponseContainer')
    const aiResponseContainer = aiResponseContainers[aiResponseContainers.length-1];
    setTimeout(function(){

     
      aiResponseContainer.innerHTML = `<div class="aiResponse">${mdText}</div>`
      scrollToBottom()
    },1000)
    
  } else {

    aiResponseContainer.innerHTML = `<div class="aiResponse">Something went wrong. Please re-try again!</div>`
    scrollToBottom();
  }
});
function scrollToBottom() {
  const aiChatContainer = document.querySelector('.aiChatContainer');
  aiChatContainer.scrollTo({
    top: aiChatContainer.scrollHeight,
    behavior: 'smooth'
  });
}
function adjustChatContainerHeight() {
  const genAiContainer = document.querySelector('.genAiContainer');
      const gradientText = document.querySelector('.gradient-text');
      const subtext = document.querySelector('.subtext');
      const prompt = document.querySelector('.prompt');
      const aiChatContainer = document.querySelector('.aiChatContainer');

      const totalHeight = genAiContainer.getBoundingClientRect().height;
      const gradientTextHeight = gradientText.getBoundingClientRect().height;
      const subtextHeight = subtext.getBoundingClientRect().height;
      const promptHeight = prompt.getBoundingClientRect().height;

 // console.log(totalHeight, gradientTextHeight, subtextHeight, promptHeight);
      const aiChatContainerHeight = totalHeight - (gradientTextHeight + subtextHeight + promptHeight+100);

      aiChatContainer.style.height = `${aiChatContainerHeight}px`;
      aiChatContainer.style.overflowY = 'scroll';
}

window.addEventListener('resize', adjustChatContainerHeight);
window.addEventListener('load', adjustChatContainerHeight);
// // Setting the Alt Text for Posted Images

