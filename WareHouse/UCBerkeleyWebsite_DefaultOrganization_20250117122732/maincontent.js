'''
This component renders the main content sections of the UC Berkeley website, including Admissions, Academics, and Research sections.
'''
import React from 'react';
function MainContent() {
    return (
        <main role="main">
            <section id="admissions" aria-labelledby="admissions-heading">
                <h2 id="admissions-heading">Admissions</h2>
                <p>Information about admissions.</p>
            </section>
            <section id="academics" aria-labelledby="academics-heading">
                <h2 id="academics-heading">Academics</h2>
                <p>Information about academics.</p>
            </section>
            <section id="research" aria-labelledby="research-heading">
                <h2 id="research-heading">Research</h2>
                <p>Information about research.</p>
            </section>
        </main>
    );
}
export default MainContent;