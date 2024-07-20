"use client"

import { ThemeSwitch } from "@/components/theme-switch";
import { Input } from "@nextui-org/input";
import {
  NavbarBrand,
  NavbarContent,
  NavbarItem,
  Navbar as NextUINavbar
} from "@nextui-org/navbar";
import { MagnifyingGlass } from "@phosphor-icons/react";
import NextLink from "next/link";
import Image from "next/image";

export const Navbar = () => (
  <NextUINavbar maxWidth="xl" position="sticky" isBordered>
    <NavbarContent justify="start">
      <NavbarBrand className="gap-3 w-fit">
        <NextLink className="flex justify-start items-center" href="/">
          <Image className="min-w-8" src="./BadTech-logo-purple.svg" width={32} height={32} alt="BadTech Logo" />
          <p className="ml-3 font-bold text-inherit text-lg hidden sm:block">Package Portal</p>
        </NextLink>
      </NavbarBrand>
    </NavbarContent>

    <NavbarContent justify="center" className="w-full mx-8">
      <NavbarItem className="flex w-full">
        <Input
          aria-label="Search"
          classNames={{
            inputWrapper: "bg-default-100 border border-default-300"
          }}
          className="w-full"
          labelPlacement="outside"
          placeholder="Search..."
          startContent={<MagnifyingGlass className="text-default-400" />}
          type="search" />
      </NavbarItem>
    </NavbarContent>

    <NavbarContent justify="end">
      <NavbarItem className="flex gap-2">
        <ThemeSwitch />
      </NavbarItem>
    </NavbarContent>
  </NextUINavbar>
);
