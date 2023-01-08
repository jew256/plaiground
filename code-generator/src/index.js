import React, {Component, useRef} from "react"
import { ReactDOM, render } from "react-dom"
import * as ReactDOMClient from 'react-dom/client';
import './index.css'


class RequestForm extends Component {
    constructor(props){
        super(props);
        this.state = {
            value: "Please enter your request here. For example: \"Graph Apple's closing price for 2020\""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event){
        this.setState({value: event.target.value})
    }

    handleSubmit(event){
        alert('A request was submitted: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                flexDirection: 'column',
                minHeight: '100%',
                minWidth: '100%',
                /* Additional CSS styles go here */
                backgroundColor: '#333333',
                borderRadius: '5px',
                boxShadow: '0px 0px 10px #000000'
              }}>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Request:&ensp;
                        <textarea value={this.state.value} onChange={this.handleChange} />
                    </label>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
}

const RequestInstructions = () => {
    return(
    <p style={{
            color: '#CCCCCC',
            fontSize: '16px',
            margin: '10px'
        }}>Please enter your request here. For example: "Graph Apple's closing price for 2020"</p>
    );
}

class FormBox extends Component{
    constructor(props){
        super(props);
        this.state = {
            request: "",
            output: "Waiting for a request",
            response: "default.png"
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event){
        this.setState({request: event.target.value})
    }

    async handleSubmit(event){
        var send_message = 'A request was submitted:\nWorking on a response. This will take a few seconds.';
        alert(send_message);
        event.preventDefault();

        var jsonData = {
            request: this.state.request
        }

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(jsonData)
        };
        const response = await fetch('https://jew256.pythonanywhere.com/code', requestOptions);
        const data = await response.json();

        await fetch('https://jew256.pythonanywhere.com/plot'  + data.responses[0])
            .then(response => response.blob())
            .then(blob => {
                // Create an object URL from the Blob
                const url = URL.createObjectURL(blob);
                this.setState({response: url}); // Update the state with the image URL
            });

            await fetch('https://jew256.pythonanywhere.com/output' + data.responses[0])
            .then(response => response.text())
            .then(text => {
                this.setState({output: text}); 
            });
    }

    render() {
        return (
            <div style={{display: 'flex', justifyContent: 'space-between'}}>
                <form style={{
                width: '50%',
                display: 'flex',
                flexDirection: 'column'
                }} onSubmit={this.handleSubmit}>
                <textarea type="text" style={{
                    fontSize: '16px',
                    minWidth: '100%',
                    width: 'auto',
                    height: 'auto',
                    minHeight: '300px',
                    overflowWrap: "break-word",
                    overflow: 'visible',
                    backgroundColor: '#555555',
                    border: 'none',
                    borderRadius: '5px',
                    padding: '10px'
                }} value = {this.state.value}  onChange={this.handleChange}/>
                <input type="submit" value="Submit" style={{
                    minWidth: '100%',
                    width: 'auto',
                    minHeight: '100px',
                    backgroundColor: '#0cf',
                    color: '#FFFFFF',
                    border: 'none',
                    borderRadius: '5px',
                    padding: '20px',
                    fontSize: '20px'
                }} />
                </form>
                <p/>
                {/* <div className="display-linebreak">{this.state.response}</div> */}
                <div style = {{width: '50%', textAlign: 'center'}}>
                    {this.state.response ? (
                        // If the image URL is available, display the image
                        <img src={this.state.response} alt="My image" />
                    ) : (
                        // Otherwise, display a loading message
                        <p>Loading image...</p>
                    )}
                    <p style={{
                        fontSize: '16px',
                        minWidth: '100%',
                        width: 'auto',
                        minHeight: '10px',
                        backgroundColor: '#555555',
                        border: 'none',
                        borderRadius: '5px',
                        padding: '10px'
                    }}> {this.state.output} </p>
                </div>
            </div>
          );
    }
  };

const App = () => {
    const interactiveRef = useRef(null);  // Create a ref for the contact me section

    function handleClick() {
        // Scroll to the contact me section when the button is clicked
        interactiveRef.current.scrollIntoView({ behavior: 'smooth' });
    }
    return (
        <>
            {/* Title bar */}
            <div className="title-bar">
            <a href="#description">Description</a>
            <a href="#interactive">Interactive</a>
            <a href="#faq">FAQ</a>
            </div>

            {/* Hero image with a contact me button */}
            <div className="hero">
                <div className="hero-overlay">
                    <h1>Plaiground</h1>
                    <p>An exploration into insights of AI</p>
                </div>
                <img src="hero.png" alt="Hero image" />
                <button className="try-button" onClick={handleClick}>Try it out!</button>
            </div>

            {/* Description section */}
            <div id="description" className="section">
                <h2>Description</h2>
                <p>In the interactive section below, you can write a request to graph financial insights. This will generate a script to access financial data online and attempt to produce the requested graph. Sometimes this will fail, and an error will be displayed. If that's the case, try changing your request to be clearer or phrased differently. It may be the case that the insight you are looking for is not accessible, so try a few times for any insight you want to see. If you are familiar with programming, the error displayed is produced by a python script, which may give you a clue into how you may better format your request.</p>
            </div>

            {/* Interactive section */}
            <div id="interactive" className="section"  ref={interactiveRef}>
                <h2>Interactive</h2>
                <RequestInstructions />
                <FormBox />
            </div>

            {/* FAQ section */}
            <div id="faq" className="section">
                <h2>FAQ</h2>
                <h3>I made a request, but the previous image hasn't changed and no error was displayed. What's wrong?</h3>
                <p>In this case a valid script was not able to be generated. Please try a differently worded request.</p>
                <h3>A graph appeared, but it's not what I was looking for. How can I graph what I want?</h3>
                <p>There's no guarantee the graphs will be correct. Sometimes a script will be written that graphs an insight that was not expected. Please try describing the insight you are looking for in more detail, especially if it is calculated from other data.</p>
                {/* Add more questions and answers as needed */}
            </div>
        </>
    );
}



const root = ReactDOMClient.createRoot(document.getElementById("root"));
root.render( <App /> );
