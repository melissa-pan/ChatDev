'''
This is the main JavaScript file for the UC Berkeley website prototype. It imports and renders the main components of the website.
'''
import React from 'react';
import Header from './Header';
import MainContent from './MainContent';
import NewsEvents from './NewsEvents';
import Footer from './Footer';
function App() {
    return (
        <div>
            <Header />
            <MainContent />
            <NewsEvents />
            <Footer />
        </div>
    );
}
export default App;