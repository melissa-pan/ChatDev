'''
This component renders the header section of the UC Berkeley website, including the logo and navigation links. It includes ARIA roles and labels for accessibility.
'''
import React from 'react';
function Header() {
    return (
        <header role="banner">
            <div className="logo" aria-label="UC Berkeley Logo">UC Berkeley</div>
            <nav role="navigation" aria-label="Main Navigation">
                <ul>
                    <li><a href="#admissions" aria-label="Admissions Section">Admissions</a></li>
                    <li><a href="#academics" aria-label="Academics Section">Academics</a></li>
                    <li><a href="#research" aria-label="Research Section">Research</a></li>
                </ul>
            </nav>
        </header>
    );
}
export default Header;