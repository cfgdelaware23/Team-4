import React from "react";
import Confetti from "react-confetti"
function Thanks(){
    return(
        <>
        
        
        
        <Confetti/>
        <div className=" flex flex-row justify-center items-center w-screen h-screen bg-ketchup"> 
        <div className= "flex flex-col justify-start items-center w-3/4  h-3/4 bg-tan  text-xl mt-40 border-2 border-black gap-20  rounded-full">
               <span className = "text-center text-8xl mt-24"><h1><span className= "text-ketchup">Well</span><span className="text-gray-500">fare </span></h1></span>

                <h1 className= "text-center text-4xl text-bold underline underline-offset-1 "> Thank you for signing up here are your next steps</h1>

                <h1 className = "text-center text-4xl text-bold" >  Please visit us at our location: </h1>
                
        </div>
        
        
        </div>
        </>




    )
        
    }

export default Thanks