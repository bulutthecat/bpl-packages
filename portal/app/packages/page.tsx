"use client"

import { PackageListing } from '@/components/package-listing';
import React, { useEffect, useState } from 'react';

export default function Page() {
  const [packages, setPackages] = useState([]);

  useEffect(() => {
    const fetchPackages = async () => {
      try {
        const response = await fetch('/api/packages');
        const data = await response.json();
        setPackages(data);
      } catch (error) {
        console.error('Error fetching packages:', error);
      }
    };

    fetchPackages();
  }, []);

  return (
    <div className="p-5 max-w-96 mx-auto">
      {packages.length > 0 ? (
        <>
          <p className="text-default-500">{packages.length} packages found</p>
          <ul>
            {packages.map((pkg, index) => (
              <li key={index}>
                <PackageListing pkg={pkg} />
              </li>
            ))}
          </ul>
        </>
      ) : (
        <p className="text-default-500">Loading packages...</p>
      )}
    </div>
  );
}
