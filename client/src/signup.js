import { React,useState, useCallback } from "react";
import { range } from "./utils/util";
import axios from 'axios';

function SignUp() {
    const FORM_PAGE_COUNT = 4;
    const [formPage, setFormPage] = useState(0);
    const pages = range(0, FORM_PAGE_COUNT);

    const [user, setUser] = useState({
        firstName: "",
        lastName: "",
        phoneNum: "",
        email: "",
        password: "",
        confirmPassword: "",
        street: "",
        city: "",
        state: "",
        zipCode: "",
        waysOfCommute: "",
        familySize: ""
    });

    //variable to handle selected image
    const [selectedImage, setSelectedImage] = useState(null);

    //function to change image when needed
    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setSelectedImage(file);
    };

    const renderFormPage = useCallback(() => {
        switch(formPage) {

            case 0: 
                return (
                    <>
                        <div className="flex flex-col justify-center items-center w-full h-full gap-10">
                        <label className="text-ketchup text-xl font-bold self-start">Image</label>
                            <input
                                type="file"
                                accept="image/*"
                                className="w-full bg-white px-4 py-2 rounded-xl"
                                onChange={handleImageChange}
                            />

                            {/* user name input */}
                            <div className="flex flex-row w-full h-24 justify-center items-center gap-5">

                                {/* first name */}
                                <div className="flex flex-col w-1/2 gap-2">
                                    <label className="text-ketchup text-xl font-bold self-start">first name</label>
                                    <input
                                        type="text"
                                        className="w-full bg-white px-4 py-7 rounded-xl"
                                        value={user.firstName}
                                        onChange={(e) => {
                                            user.firstName = e.target.value;
                                            setUser(user => ({...user, firstName: e.target.value}));
                                            console.log(user);
                                        }}
                                    >
                                    </input>
                                </div>

                                {/* last name */}
                                <div className="flex flex-col w-1/2 gap-2">
                                    <label className="text-ketchup text-xl font-bold self-start">last name</label>
                                    <input
                                        type="text"
                                        className="w-full bg-white px-4 py-7 rounded-xl"
                                        value={user.lastName}
                                        onChange={(e) => {
                                            user.lastName = e.target.value;
                                            setUser(user => ({...user, lastName: e.target.value}));
                                        }}
                                    >
                                    </input>
                                </div>

                            </div>

                            {/* phone number input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">phone number</label>
                                <input
                                    type="tel"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.phoneNum}
                                    onChange={(e) => {
                                        user.phoneNum = e.target.value;
                                        setUser(user => ({...user, phoneNum: e.target.value}));
                                    }}
                                >
                                </input>
                            </div>

                        </div>
                    </>
                );
            
            case 1: 
                return (
                    <>
                        <div className="flex flex-col justify-center items-center w-full h-full gap-10">

                            {/* email input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">email</label>
                                <input
                                    type="email"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.email}
                                    onChange={(e) => {
                                        user.email = e.target.value;
                                        setUser(user => ({...user, email: e.target.value}));
                                    }}
                                >
                                </input>
                            </div>

                            {/* password input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">password</label>
                                <input
                                    type="password"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.password}
                                    onChange={(e) => {
                                        user.password = e.target.value;
                                        setUser(user => ({...user, password: e.target.value}));
                                    }}
                                >
                                </input>
                            </div>

                            {/* confirm password input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">confirm password</label>
                                <input
                                    type="password"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.confirmPassword}
                                    onChange={(e) => {
                                        user.confirmPassword = e.target.value;
                                        setUser(user => ({...user, confirmPassword: e.target.value}));
                                    }}
                                >
                                </input>
                            </div>

                        </div>
                    </>
                );

            case 2: 
                return (
                    <>
                        <div className="flex flex-col justify-center items-center w-full h-full gap-10">

                            {/* street input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">street</label>
                                <input
                                    type="text"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.street}
                                    onChange={(e) => {
                                        user.street = e.target.value;
                                        setUser(user => ({...user, street: e.target.value}));
                                    }}
                                >
                                </input>
                            </div>

                            {/* city input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">city</label>
                                <input
                                    type="text"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.city}
                                    onChange={(e) => {
                                        user.city = e.target.value;
                                        setUser(user => ({...user, city: e.target.value}));
                                    }}
                                >
                                </input>
                            </div>

                            {/* state / zip name input */}
                            <div className="flex flex-row w-full h-24 justify-center items-center gap-5">

                                {/* state */}
                                <div className="flex flex-col w-1/2 gap-2">
                                    <label className="text-ketchup text-xl font-bold self-start">state</label>
                                    <input
                                        type="text"
                                        className="w-full bg-white px-4 py-7 rounded-xl"
                                        value={user.state}
                                        onChange={(e) => {
                                            user.state = e.target.value;
                                            setUser(user => ({...user, state: e.target.value}));
                                        }}
                                    >
                                    </input>
                                </div>

                                {/* zip code */}
                                <div className="flex flex-col w-1/2 gap-2">
                                    <label className="text-ketchup text-xl font-bold self-start">zip code</label>
                                    <input
                                        type="text"
                                        className="w-full bg-white px-4 py-7 rounded-xl"
                                        value={user.zipCode}
                                        onChange={(e) => {
                                            user.zipCode = e.target.value;
                                            setUser(user => ({...user, zipCode: e.target.value}));
                                        }}
                                    >
                                    </input>
                                </div>

                            </div>

                        </div>
                    </>
                );
            
            case 3: 
                return (
                    <>
                        <div className="flex flex-col justify-center items-center w-full h-full gap-10">

                            {/* commute ways input */}
                            <div className="flex flex-col w-full gap-2">
                                <label className="text-ketchup text-xl font-bold self-start">ways of commute</label>
                                <input
                                    type="text"
                                    className="w-full bg-white px-4 py-7 rounded-xl"
                                    value={user.waysOfCommute}
                                    onChange={(e) => {
                                        user.waysOfCommute = e.target.value;
                                        setUser(user => ({...user}));
                                    }}
                                >
                                </input>
                            </div>

                            {/* number of family members input */}
                            <div className="flex flex-row w-full h-24 justify-center items-center gap-5">

                                {/* famliy size */}
                                <div className="flex flex-col items-start w-full gap-2">
                                    <label className="text-ketchup text-xl font-bold">family size</label>
                                    <input
                                        type="text"
                                        className="w-1/2 bg-white px-4 py-7 rounded-xl"
                                        value={user.familySize}
                                        onChange={(e) => {
                                            user.familySize = e.target.value;
                                            setUser(user => ({...user}));
                                        }}
                                    >
                                    </input>
                                </div>

                            </div>

                        </div>
                    </>
                );
        }
    }, [formPage]);
    
    const sendUserToFlask = () => {
        const formData = new FormData();
        formData.append('image', selectedImage); // Append the image file
        formData.append('user', JSON.stringify(user)); // Convert user data to JSON and append


        axios.post('/sign-up', formData, {
            headers: {
              'Content-Type': 'multipart/form-data', // Set the Content-Type header
            },
          })
            .then((response) => {
                console.log(response.data.message);
            })
            .catch((error) => {
                console.error(error);
            })
    }

    const PageIndexMarker = ({ id }) => {
        return (
            <>
            
                {
                    id != formPage ? (
                        <div className="w-5 h-5 bg-white rounded-full"/>
                    ) : (
                        <div className="w-5 h-5 bg-ketchup rounded-full"/>
                    )
                }
            
            </>
        )
    }

    return (
        <div className="flex flex-row w-screen h-screen bg-white">

            {/* sign up graphic */}
            <div className="flex justify-end items-center w-1/2 h-full bg-ketchup">
                <h1 className="text-white text-8xl font-bold text-right p-16">sign <br/> up</h1>
            </div>

            {/* form for user input */}
            <div className="flex flex-col justify-between items-center w-1/2 h-full bg-tan px-16 py-14 gap-5">

                <form className="w-full h-full p-4">
                    {renderFormPage()}
                </form>

                <div className="flex flex-col w-full h-16 justify-between items-center gap-5">

                    <div className="flex flex-row w-full h-16 justify-between items-center gap-5">
                        {/* back button */}
                        {
                            formPage != 0 ? (
                                <button 
                                    className="w-1/3 h-16 bg-ketchup rounded-xl"
                                    onClick={(e) => {
                                        e.preventDefault();
                                        setFormPage((prev) => prev - 1);
                                    }}
                                >
                                    <h1 className="text-white text-3xl font-bold">back</h1>
                                </button>
                            ) : (
                                <div className="w-1/3 h-16 bg-tan"/>
                            )
                        }

                        {/* next / submit button */}
                        {
                            formPage != FORM_PAGE_COUNT - 1 ? (
                                <button 
                                    className= "w-1/3 h-16 bg-ketchup rounded-xl"
                                    onClick={(e) => {
                                        e.preventDefault(); 
                                        setFormPage((prev) => prev + 1);
                                    }}
                                >
                                    <h1 className="text-white text-3xl font-bold">next</h1>
                                </button>
                            ) : (
                                <button 
                                    className= "w-1/3 h-16 bg-ketchup rounded-xl"
                                    onClick={sendUserToFlask}
                                >
                                    <h1 className="text-white text-3xl font-bold">submit</h1>
                                </button>
                            )
                        }
                    </div>

                    <div className="flex flex-row justify-center gap-5 w-full h-10">
                        {
                            pages.map((id) => (
                                <PageIndexMarker id={id}/>
                            ))
                        }
                    </div>

                </div>
            </div>
        </div>
    );
}
  
export default SignUp;