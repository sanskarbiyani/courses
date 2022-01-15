import React, { useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import CreateArea from "./CreateArea";

function App(){
    const [notes, setNotes] = useState([{
        title: "Peace",
        content: "Movie Apreciation"
    },{
        title: "Math",
        content: "Tutorial"
    }]);

    function addNote(note){
        setNotes( prevValue => {
            return [
                ...prevValue,
                note
            ]
        })
    }

    function DeleteNote(id){
        setNotes( prevValue => {
            return prevValue.filter( (value, index)=>{
                return index !== id;
            })
        })
    }

    return(
        <div>
    <Header />
    <CreateArea add={addNote} />
    { notes.map( (note, index) => ( 
        <Note key={index} id={index} title={note.title} content={note.content} delete={DeleteNote} />
    )) }
    
    <Footer />
    </div>
    );
};

export default App;