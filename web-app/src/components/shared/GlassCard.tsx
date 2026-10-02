import { cn } from "@/lib/utils";

export default function GlassCard({
  className,
  children,
}: {
  className?: string;
  children: React.ReactNode;
}) {
  return (
    <div
      className={cn(
        "glass rounded-2xl p-6 shadow-xl shadow-black/5",
        "animate-fade-in",
        className,
      )}
    >
      {children}
    </div>
  );
}
