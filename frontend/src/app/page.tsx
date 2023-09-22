// @ts-nocheck
'use client';
import React, {useState, useEffect, useRef} from "react";

const BaseURL = "/api/events";

function App() {

    const [loading, setLoading] = useState(false);
    const textContainer = useRef<HTMLDivElement>(null);
    const index = useRef(-1);

    useEffect(() => {
        setLoading(true)
        const eventSource = new EventSource(BaseURL);
        eventSource.onmessage = (e) => {
            index.current += 1;
            if (e.data === "end") {
                setLoading(false)
                eventSource.close();
            } else textContainer.current.innerText += index === 0 ? e.data : ` ${e.data}`;
        }
        eventSource.onerror = (e) => {
            console.error("EventSource failed:", e);
            eventSource.close();
            setLoading(false)
        }
        return () => {
            eventSource.close();
            setLoading(false)
        }
    }, []);

    return (
        <div className="flex flex-col items-center justify-center h-screen overflow-hidden">
            <div className="font-bold text-transparent text-5xl bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600">
                Server Sent Events
            </div>
            <div className="relative border min-h-[300px] w-[500px] rounded-lg mt-4 border-gray-300/50 p-4 break-all">
                <span ref={textContainer} />
                {loading && (
                    <div
                        className="inline-block h-4 w-4 animate-spin rounded-full border-2 border-solid border-current border-r-transparent align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite] absolute bottom-2 left-2"
                        role="status"
                    />
                )}
            </div>
        </div>
    );
}export default App