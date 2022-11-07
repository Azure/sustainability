import React from 'react';
import Navbar from '@theme-original/Navbar';

export default function NavbarWrapper(props) {
  return (
    <>
      <p style={{ background: '#f0ffc4', textAlign: 'center', padding: '16px 32px', color: 'var(--ifm-color-primary-dark)', fontWeight: 'bold' }}>You are viewing a Microsoft open source community project that is currently in draft state. This project should not be considered finished or officially supported in any way by Microsoft.</p>
      <Navbar {...props} />
    </>
  );
}
