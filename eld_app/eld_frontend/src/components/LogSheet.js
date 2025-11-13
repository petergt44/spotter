import React from 'react';

const LogSheet = ({ logSheet }) => {
    return (
        <div className="log-sheet">
            <h3>{logSheet.date}</h3>
            <div className="grid">
                {logSheet.grid.map((entry, index) => (
                    <div
                        key={index}
                        className={`status-${entry.status.replace(' ', '-')}`}
                        style={{
                            left: `${(entry.start - (logSheet.grid[0].start)) * 20}px`,
                            width: `${(entry.end - entry.start) * 20}px`,
                        }}
                    >
                        {entry.status}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default LogSheet;