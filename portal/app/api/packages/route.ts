import path from "path";
import fs from 'fs';

export async function GET() {
  try {
    const files = fs.readdirSync(path.join(process.cwd(), '../lib'), { withFileTypes: true });

    const packages = files
      .filter(file => file.isDirectory())
      .map(file => file.name);

    return Response.json(packages);
  } catch {
    return Response.json({error: "Something went wrong"}, {status: 500});
  }
}