import { writable } from "svelte/store";

export const getTest = 'http://localhost:5000/test';

export const dataStoreName = writable('');