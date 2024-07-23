import path from "path";
import fs from 'fs';
import Fuse from "fuse.js";

export async function GET(req: Request) {
  let query = new URLSearchParams(req.url.split('?')[1]).get('query');

  try {
    const files = fs.readdirSync(path.join(process.cwd(), '../lib'), { withFileTypes: true });

    const packages = files
      .filter(file => file.isDirectory())
      .map(file => file.name)

    if (!query) return Response.json(packages);

    const fuse = new Fuse(packages);
    const results = fuse.search(query);

    const matchedPackages = results.map(result => result.item);

    return Response.json(matchedPackages);
  } catch {
    return Response.json({ error: "Something went wrong" }, { status: 500 });
  }
}