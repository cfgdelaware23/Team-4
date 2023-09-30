
import{Link} from "react-router-dom"
export default function Root(){
    function clicked(){
        alert("You clicked me")
    }
  
        return (
      
            <div className="flex flex-row justify-center items-center w-screen h-screen bg-ketchup">
    
    
    
                
    <div className= "flex flex-col justify-start items-center w-1/2 h-1/2 bg-tan  text-xl mt-40 border-2 border-black gap-20">
    
       <span className = "text-center text-8xl mt-24"><h1><span className= "text-ketchup">Well</span><span className="text-gray-500">fare </span></h1></span>
    
     
        
        <nav>
        <button onClick = {clicked} className="w-1/2 h 1/2 rounded-xl border-4 border-black border-solid
            text-tan bg-ketchup font-bold text-4xl gap-right-4"><Link to = "/sign">Signup </Link></button>
        
        <button onClick = {clicked} className="w-1/2 h 1/3 rounded-xl border-4 border-black border-solid
            text-tan bg-ketchup font-bold text-4xl">       Login
        </button>
        
         
        </nav>
           
    
    
    
   
    
        
    </div>
    
    </div>
        
    
            
            
            
            
            
            
    
        
        )


    



}