import React, { useState } from "react";

function CreateArea(props){
    const [noteBody, setNoteBody] = useState({
        title: "",
        content: ""
    });

    function handleChange(event){
        const {name, value} = event.target;
        setNoteBody(prevValue=>{
            return {
                ...prevValue,
                [name]: value
            };
        });
    };

    return (
        <div>
            <form>
                <input 
                    type="text" 
                    name="title" 
                    onChange={handleChange} 
                    placeholder="Title" 
                    value={noteBody.title} 
                />
                <input 
                    type="text" 
                    name="content"
                    onChange={handleChange} 
                    placeholder="Enter notes body..." 
                    value={noteBody.content} 
                />
                <button onClick={ (event) =>{
                    props.add(noteBody);
                    event.preventDefault();
                    setNoteBody({
                        title: "",
                        content: ""
                    })
                }} >Add</button>
            </form>
        </div>
    )
}

export default CreateArea;