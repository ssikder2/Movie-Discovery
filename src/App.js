import userEvent from '@testing-library/user-event';
import React, { useState, useEffect, useRef } from 'react'
  
function App() {

  const [comments, setComments] = useState([])
  const [inputText, setInputText] = useState("");


  useEffect(() => {
    fetch("/comments").then(response =>
      response.json().then(data => {
        setComments(data)
      })
    )
  }, [])

  function handleClick() {
    const val = inputRef.current.value;
    const newComments = [...comments, val];
    setComments(newComments);
    inputRef.current.value = "";
  }

  function handleRemove(id){
    fetch('/comment/'+id, {
      method: 'DELETE',
      header: {
         'Accept' : 'application/json',
         'Content-Type' : 'application/json',
        }
      })
      setComments(comments.filter(comment => comment.id !== id))
 }


  return (
    <div className="App">
      { <button onClick={() =>  console.log(comments)}>Comments</button> }

      { <table>
        <tr>
          <th>Movie ID: </th>
          <th>Rating: </th>
          <th>Review: </th>
        </tr>
        {comments.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.movie}</td>
              <td><input
                      type="text"
                      value={val.rating}
                      onChange={(e) => setInputText(e.target.value)}
                    /></td>
              <td>{val.review}</td>
              <td><button onClick={() => handleRemove(val.id)}>Delete</button></td>
            </tr>
          )
        })}
        <button onClick={handleClick}>Save Changes</button>
      </table> }
    </div>
  );
}

export default App