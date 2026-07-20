import React from 'react';
import { Loader2 } from 'lucide-react';

export const Card = ({ children, className = "" }) => (
  <div className={`glass-card p-6 ${className}`}>
    {children}
  </div>
);

export const Button = ({ children, variant = "primary", className = "", isLoading, ...props }) => {
  const baseClass = variant === "primary" ? "primary-btn" : "secondary-btn";
  return (
    <button className={`${baseClass} flex items-center justify-center gap-2 ${className}`} disabled={isLoading || props.disabled} {...props}>
      {isLoading && <Loader2 className="w-4 h-4 animate-spin" />}
      {children}
    </button>
  );
};
