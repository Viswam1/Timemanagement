// Minimal client stub. Talks to the Chronos MCP server if configured.
// For production, use @modelcontextprotocol/sdk with SSE transport.

const MCP_URL = process.env.NEXT_PUBLIC_MCP_URL;

export async function callTool<T = unknown>(
  tool: string,
  args: Record<string, unknown>,
): Promise<T | null> {
  if (!MCP_URL) return null;
  try {
    const res = await fetch(`${MCP_URL}/tools/${tool}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(args),
    });
    if (!res.ok) return null;
    return (await res.json()) as T;
  } catch {
    return null;
  }
}
