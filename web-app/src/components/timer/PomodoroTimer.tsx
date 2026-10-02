"use client";

import { useEffect, useRef, useState } from "react";
import GlassCard from "@/components/shared/GlassCard";
import { Play, Pause, RotateCcw } from "lucide-react";

export default function PomodoroTimer() {
  const [task, setTask] = useState("Deep work");
  const [focusMin, setFocusMin] = useState(25);
  const [breakMin, setBreakMin] = useState(5);
  const [seconds, setSeconds] = useState(25 * 60);
  const [running, setRunning] = useState(false);
  const [phase, setPhase] = useState<"focus" | "break">("focus");
  const [rounds, setRounds] = useState(0);
  const tick = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    if (!running) return;
    tick.current = setInterval(() => {
      setSeconds((s) => {
        if (s > 1) return s - 1;
        // phase switch
        if (phase === "focus") {
          setPhase("break");
          setRounds((r) => r + 1);
          return breakMin * 60;
        }
        setPhase("focus");
        return focusMin * 60;
      });
    }, 1000);
    return () => { if (tick.current) clearInterval(tick.current); };
  }, [running, phase, focusMin, breakMin]);

  const total = (phase === "focus" ? focusMin : breakMin) * 60;
  const progress = 1 - seconds / total;
  const pct = Math.round(progress * 100);
  const mm = String(Math.floor(seconds / 60)).padStart(2, "0");
  const ss = String(seconds % 60).padStart(2, "0");

  function reset() {
    setRunning(false);
    setPhase("focus");
    setSeconds(focusMin * 60);
  }

  return (
    <GlassCard className="mx-auto max-w-xl">
      <p className="text-sm uppercase tracking-widest opacity-60">
        {phase === "focus" ? "Focus" : "Break"} · Round {rounds + 1}
      </p>
      <p className="mt-2 text-6xl font-bold tabular-nums">
        {mm}:{ss}
      </p>

      <div className="mt-4 h-2 w-full overflow-hidden rounded-full bg-black/10 dark:bg-white/10">
        <div
          className="h-full rounded-full transition-all"
          style={{ width: `${pct}%`, background: "#e63946" }}
        />
      </div>

      <div className="mt-6 grid gap-3 sm:grid-cols-3">
        <label className="text-sm">
          Task
          <input
            value={task}
            onChange={(e) => setTask(e.target.value)}
            className="mt-1 w-full rounded-lg bg-black/5 px-3 py-2 outline-none dark:bg-white/10"
          />
        </label>
        <label className="text-sm">
          Focus (min)
          <input
            type="number" min={1} value={focusMin}
            onChange={(e) => { const v = +e.target.value || 1; setFocusMin(v); if (!running && phase === "focus") setSeconds(v * 60); }}
            className="mt-1 w-full rounded-lg bg-black/5 px-3 py-2 outline-none dark:bg-white/10"
          />
        </label>
        <label className="text-sm">
          Break (min)
          <input
            type="number" min={1} value={breakMin}
            onChange={(e) => setBreakMin(+e.target.value || 1)}
            className="mt-1 w-full rounded-lg bg-black/5 px-3 py-2 outline-none dark:bg-white/10"
          />
        </label>
      </div>

      <div className="mt-6 flex justify-center gap-3">
        <button
          onClick={() => setRunning((r) => !r)}
          className="flex items-center gap-2 rounded-xl bg-[#e63946] px-5 py-2.5 font-medium text-white transition hover:brightness-110"
        >
          {running ? <Pause size={18} /> : <Play size={18} />}
          {running ? "Pause" : "Start"}
        </button>
        <button
          onClick={reset}
          className="flex items-center gap-2 rounded-xl bg-black/5 px-5 py-2.5 font-medium transition hover:bg-black/10 dark:bg-white/10 dark:hover:bg-white/20"
        >
          <RotateCcw size={18} /> Reset
        </button>
      </div>

      <p className="mt-4 text-center text-xs opacity-60">
        Working on <span className="font-medium">{task}</span> · {rounds} completed round{rounds === 1 ? "" : "s"}
      </p>
    </GlassCard>
  );
}
