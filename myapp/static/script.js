async function uploadFile(file) {
  let server = ''; // Variable to store server name

  try {
    // Fetch server names
    const serverResponse = await fetch('https://api.gofile.io/servers', {
      method: 'GET'
    });
    const serverData = await serverResponse.json();
    console.log(serverData);

    if (serverData.status === 'ok') {
      server = serverData.data.servers[0].name; // Assuming we take the first server in the list
    }
  } catch (error) {
    console.error('Error fetching server data:', error);
    return { status: 'error', message: 'Error fetching server data' };
  }

  const formData = new FormData();
  formData.append('file', file);

  const token = 'WRjylhki7EGXkpmXPPLuVVKwknAIcVp3'; // Replace with your actual token

  try {
    const response = await fetch(`https://${server}.gofile.io/uploadFile`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`
      },
      body: formData,
    });
    const data = await response.json();
    console.log(data);

    if (data.status === 'ok') {
      const downloadLink = data.data.downloadPage;
      return { status: 'ok', downloadLink };
    } else {
      return { status: 'error', message: `Error uploading file: ${data.error}` };
    }
  } catch (error) {
    console.error('Error uploading file:', error);
    return { status: 'error', message: 'Error uploading file' };
  }
}

// Function to handle button click
function handleUpload() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];

  if (!file) {
    alert('Please select a file to upload.');
    return;
  }

  uploadFile(file)
    .then(uploadResult => {
      if (uploadResult.status === 'ok') {
        const downloadLink = uploadResult.downloadLink;
        document.getElementById('response').innerHTML = `
          <p>File uploaded successfully!</p>
          <p>Copy the following link and paste it in the ppt link box.</p>
          <p>Copy this link : <span id="downloadLink">${downloadLink}</span></p>
        `;
      } else {
        document.getElementById('response').innerHTML = `<p>${uploadResult.message}</p>`;
      }
    })
    .catch(err => {
      console.error('Error during upload:', err);
      document.getElementById('response').innerHTML = `<p>Error during upload. Please try again.</p>`;
    });
}

// Attach click event to the button
document.getElementById('uploadButton').addEventListener('click', handleUpload);
