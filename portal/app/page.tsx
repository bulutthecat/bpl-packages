"use client"

import { siteConfig } from "@/config/site";
import { Button } from "@nextui-org/button";
import { Code } from "@nextui-org/code";
import { Input } from "@nextui-org/input";
import { Link } from "@nextui-org/link";
import { MagnifyingGlass } from "@phosphor-icons/react";

export default function Home() {
  return (
    <div>
      <section className="bg-gradient-to-br from-emerald-300 to-sky-400 dark:from-emerald-500 dark:to-sky-600 py-16">
        <div className="text-center items-center flex flex-col container mx-auto gap-12">
          <h1 className="text-4xl">Explore BadOS packages with the <span className="font-semibold">Package Portal</span></h1>

          <div className="flex sm:w-[512px] gap-2">
            <Input
              aria-label="Search"
              classNames={{
                label: "text-black/50 dark:text-white/90",
                input: [
                  "bg-transparent",
                  "text-black/90 dark:text-white/90",
                  "placeholder:text-default-700/60 dark:placeholder:text-white/60",
                ],
                innerWrapper: "bg-transparent",
                inputWrapper: [
                  "shadow-xl",
                  "bg-default-200/50",
                  "dark:bg-default/60",
                  "backdrop-blur-xl",
                  "backdrop-saturate-200",
                  "hover:bg-default-200/70",
                  "dark:hover:bg-default/70",
                  "group-data-[focus=true]:bg-default-200/50",
                  "dark:group-data-[focus=true]:bg-default/60",
                  "!cursor-text",
                ]
              }}
              className="max-w-[512px]"
              labelPlacement="outside"
              placeholder="Search the BadOS Package Portal..."
              startContent={<MagnifyingGlass className="text-default-600/60" />}
              type="search"
            />

            <Button color="primary">
              Search
            </Button>
          </div>

          <p>Or, <Link href="/packages" color="foreground" underline="hover" className="font-semibold">browse all packages</Link>.</p>
        </div>
      </section>

      <section className="max-w-[64rem] mx-auto space-y-4 py-8">
        <h1 className="text-2xl font-semibold">What is the BadOS Package Portal?</h1>
        <p>The BadOS Package Portal is an online application to index and browse the BadOS Dynamic Shell Package Library (BPL). The BPL contains a library of software for BDSH, shared by first-party developers and the community.</p>
        <p>The creation, publication, etc. of BadOS packages is documented <Link href={siteConfig.links.docs.bpl} color="foreground" underline="always" className="font-semibold" isExternal>here</Link>.</p>
      </section>

      <section className="max-w-[64rem] mx-auto space-y-4 py-8">
        <h1 className="text-2xl font-semibold">Package Management (installation, removal, etc.)</h1>
        <p>To download, install, remove, or otherwise manage your packages, use the BadOS Package Manager (BPM) tool.</p>
        <p>All installations of BDSH should have the latest version of BPM. If you don't, setup the system again, or manually download it if you're up to it.</p>
        <div className="space-y-1">
          <p className="text-sm text-default-600">Install a package</p>
          <Code>bpm install &lt;package name&gt;</Code>
        </div>
        <div className="space-y-1">
          <p className="text-sm text-default-600">Uninstall a package</p>
          <Code>bpm remove &lt;package name&gt;</Code>
        </div>
      </section>
    </div>
  );
}
