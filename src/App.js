import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

function App() {

  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetch('/comments').then(response => 
      response.json().then(data => {
        setComments(data);
      })
    );
  }, []);

  function handleRemove(id) {
    fetch('/comment/' + id, {
      method: 'DELETE',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    });
    setComments(comments.filter(comment => comment.id !== id));
  }

  function handleRating() {
    const [rating, setRating] = useState('');
  }

  return (
    <div className='main'>
      <table>
        <tr>
          <th>Movie ID: </th>
          <th>Rating: </th>
          <th>Review: </th>
        </tr>
        {comments.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.movie}</td>
              <td><input type='text' value={val.rating}/> </td>
              <td>{val.review}</td>
              <td><button onClick={() => handleRemove(val.id)}>Delete!</button></td>
            </tr>
          );
        })}
        <button onClick={() => alert('Save Succesful!')}>Save Changes</button>
      </table>
    </div>
  );
}

ReactDOM.render(<handleRating />, document.getElementById('root'));

export default App;
