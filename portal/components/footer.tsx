"use client"

import { GithubLogo, XLogo } from "@phosphor-icons/react";
import Image from "next/image";
import Link from "next/link";

export const Footer = () => (
  <footer className="text-default-600 body-font">
    <div className="container px-5 py-24 mx-auto flex md:items-center lg:items-start md:flex-row md:flex-nowrap flex-wrap flex-col">
      <div className="w-64 flex-shrink-0 md:mx-0 mx-auto text-center md:text-left">
        <a className="flex title-font font-medium items-center md:justify-start justify-center text-default-900">
          <Image className="min-w-8" src="./BadTech-logo-purple.svg" width={32} height={32} alt="BadTech Logo" />
          <span className="ml-3 text-xl">BadOS Package Portal</span>
        </a>
        <p className="mt-2 text-sm text-default-500">Powered by the BadOS Dynamic Shell Package Library (BPL).</p>
        <p className="mt-2 text-sm text-default-500">BPL contains user-uploaded content. Packages are verified by the BadTech before publishing to BPL.</p>
      </div>
      <div className="flex-grow flex flex-wrap md:pl-20 -mb-10 md:mt-0 mt-10 md:text-left text-center">
        <div className="lg:w-1/4 md:w-1/2 w-full px-4">
          <h2 className="title-font font-medium text-default-900 tracking-widest text-sm mb-3">Documentation</h2>
          <nav className="list-none mb-10 text-default-600">
            <li>
              <Link className="hover:text-default-800 hover:underline" href="https://badtechnologies.github.io/bdsh/">BadOS Dynamic Shell (BDSH)</Link>
            </li>
            <li>
              <Link className="hover:text-default-800 hover:underline" href="https://badtechnologies.github.io/bdsh/bpl.html">BDSH Package Library (BPL)</Link>
            </li>
            <li>
              <Link className="hover:text-default-800 hover:underline" href="https://badtechnologies.github.io/bdsh/bpm.html">BadOS Package Manager (BPM)</Link>
            </li>
          </nav>
        </div>
      </div>
    </div>
    <div className="bg-default-100">
      <div className="container mx-auto py-4 px-5 flex flex-wrap text-default-500 text-sm">
        <p>© {new Date().getFullYear()} | Bad Technologies</p>
        <span className="inline-flex ml-auto justify-start gap-2">
          <Link href="https://github.com/badtechnologies">
            <GithubLogo size={20} />
          </Link>
          <Link href="https://x.com/badtechnologies">
            <XLogo size={20} />
          </Link>
        </span>
      </div>
    </div>
  </footer>
);